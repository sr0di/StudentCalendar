# from datetime import datetime, timedelta
from calendar import HTMLCalendar

from django.http import request
from django.urls import reverse

from .models import Repart
# from ..accounts.models import Profil


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, profil=None):
        self.profil = profil
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, weekday, activitati):
        activitati_pe_zi = activitati.filter(zi__cod=weekday)
        d = ''
        for activitate in activitati_pe_zi:
            url = reverse('cal:activitate_detail',kwargs={'pk':activitate.id})
            # url = "{% url 'cal:activitate_detail' {activitate.id} %}"
            d += f"""<li><a href="{url}"> {activitate.disciplina.denr}, {activitate.ora_i}-{activitate.ora_s} </a></li>"""

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, activitati):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, weekday, activitati)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True, **kwargs):
        grupa = str(self.profil.grupa)
        activitati = Repart.objects.filter(semestru__data_inceput__year=self.year, formatie__componenta__contains=grupa)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, activitati)}\n'
        return cal

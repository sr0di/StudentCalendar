# from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Repart
# from ..accounts.models import Profil


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, weekday, activitati):
        activitati_pe_zi = activitati.filter(zi__cod=weekday)
        d = ''
        for activitate in activitati_pe_zi:
            d += f'<li> {activitate.disciplina.denr} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, activitati):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, weekday, activitati)
        return f'<tr> {week} </tr>'

    def formatweekheader(self):
        pass

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True, **kwargs):
        activitati = Repart.objects.filter(semestru__data_inceput__year=self.year)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, activitati)}\n'
        return cal

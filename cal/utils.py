import datetime
from calendar import HTMLCalendar
from django.urls import reverse


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, profil=None):
        self.profil = profil
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, weekday, activitati):
        vacanta = False
        ok = False
        d = ''

        if day != 0:
            current_date = datetime.date(self.year, self.month, day)
            if activitati:
                activitati_pe_zi = activitati.filter(disciplina__zi__cod=weekday)
                semestru = activitati.first().disciplina.semestru
                if semestru.data_inceput <= current_date <= semestru.data_sfarsit:
                    ok = True
                structura_semestru = semestru.structuri_semestru.filter(limbi_predare__denr=self.profil.limba_predare.denr).first()
                activitati_nedidactice = structura_semestru.activitati_nedidactice.filter(data_inceput__lte=current_date,
                                                                                          data_sfarsit__gte=current_date)
                if activitati_nedidactice:
                    vacanta = True
                    d += f"""<li> {activitati_nedidactice.first().descriere}</li>"""
                if activitati_pe_zi:
                    pass

                for activitate in activitati_pe_zi:
                    if not vacanta:
                        if ok:
                            activitate_didactica = activitate.disciplina
                            url = reverse('cal:activitate_detail', kwargs={'pk': activitate.id})
                            d += f"""<li><a href="{url}"> {activitate_didactica.tip_activitate}: {activitate_didactica.disciplina.denr}, {activitate_didactica.ora_i}-{activitate_didactica.ora_s} </a></li>"""

            if day == datetime.date.today().day:
                return f"<td><span class='date badge'>{day}</span><ul> {d} </ul></td>"
            else:
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

        activitati = self.profil.activitati.filter(
            disciplina__semestru__data_inceput__year=self.year,
            disciplina__semestru__data_inceput__month__lte=self.month,
            disciplina__semestru__data_sfarsit__month__gte=self.month,
            hidden=False)

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, activitati)}\n'
        return cal

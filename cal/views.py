
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.utils.safestring import mark_safe
from django.views.generic import DetailView

from accounts.models import Profil
from .models import *
from .utils import Calendar


class CalendarView(generic.ListView):
    '''login_url = 'accounts:login'
    redirect_field_name = 'redirect_to'''
    model = Repart
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        profil = Profil.objects.filter(user_id=user_id).first()

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month, profil)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.today()


class ActivitateDetailView(DetailView):
    template_name = 'cal:activitate_detail.html'
    queryset = Repart.objects.all()

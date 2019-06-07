import calendar
from datetime import timedelta
import datetime

from django.shortcuts import redirect, render
from django.views import generic
from django.utils.safestring import mark_safe
from django.views.generic import DetailView, ListView
from accounts.models import Profil, Activitate
from .models import *
from .utils import Calendar


class CalendarView(generic.ListView):
    model = Repart
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        profil = Profil.objects.filter(user_id=user_id).first()
        context['id_profil'] = profil.id

        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month, profil)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.date.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def change_group(request, old_pk, new_pk):
    new_disc = Repart.objects.get(pk=new_pk)
    Activitate.objects.create(profil=request.user.profil, disciplina=new_disc)
    old_disc = Repart.objects.get(pk=old_pk)
    Activitate.objects.filter(profil=request.user.profil, disciplina=old_disc).delete()

    return redirect('cal:disciplina_list')


def list_group(request, pk):
    disc = Repart.objects.get(pk=pk)
    denumire = disc.disciplina.denr
    componenta = disc.formatie.componenta
    discipline = Repart.objects.filter(disciplina__denr=denumire, tip_activitate=disc.tip_activitate).exclude(formatie__componenta=componenta)
    error = 'Nu exista alte grupe!'
    return render(request, 'cal/change_group.html', context={'discipline': discipline, 'current_disc': disc, 'error':error })


def hide(request, pk):
    activitate = Activitate.objects.filter(id=pk).first()
    if activitate:
        if not activitate.hidden:
            activitate.hidden = True
        else:
            activitate.hidden = False
        activitate.save()
        return redirect('cal:disciplina_list')
    error = 'Activitatea pe care vreti sa o ascundeti nu exista!'
    return redirect('cal:disciplina_list', context={'error': error, })


class DisciplinaListView(ListView):
    template_name = 'cal/disciplina_list.html'
    context_object_name = 'activitati'

    def get_queryset(self):
        return Activitate.objects.filter(profil_id=self.request.user.profil)


class ActivitateDetailView(DetailView):
    template_name = 'cal/activitate_detail.html'

    def get_queryset(self):
        return Activitate.objects.filter(profil_id=self.request.user.profil)

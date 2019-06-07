from django.contrib.auth.decorators import login_required
from django.urls import path, include

from . import views


app_name = 'cal'
urlpatterns = [
    path(r'', login_required(views.CalendarView.as_view()), name='calendar'),
    path(r'activitate/<int:pk>/', views.ActivitateDetailView.as_view(), name='activitate_detail'),
    path(r'list_discipline/', views.DisciplinaListView.as_view(), name='disciplina_list'),
    path(r'ascunde/<int:pk>/', views.hide, name="hide"),
    path(r'schimba-seminar/<int:pk>/', views.list_group, name="list_group"),
    path(r'schimba-grupa/<int:old_pk>/<int:new_pk>/', views.change_group, name="change_group"),
]

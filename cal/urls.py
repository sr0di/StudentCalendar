from django.urls import path, include

from . import views


app_name = 'cal'
urlpatterns = [
    path(r'user<int:pk>/', views.CalendarView.as_view(), name='calendar'),
    path(r'activitate/<int:pk>/', views.ActivitateDetailView.as_view(), name='activitate_detail'),
]

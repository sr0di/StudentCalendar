from django.urls import path, include
from .views import (
    register, ProfileUpdateView,
    load_limba_predare, login_view,
    load_an, load_grupa
)


urlpatterns = [
    path(r'', register, name='register'),
    path(r'login/', login_view, name="login_view"),
    path(r'profil<int:pk>/', ProfileUpdateView.as_view(), name='profil_change'),
    path(r'calendar/', include('cal.urls'), name='planner'),




    path('ajax/load-lb/', load_limba_predare, name='ajax_load_lb'),
    path('ajax/load-an/', load_an, name='ajax_load_an'),
    path('ajax/load-grupa/', load_grupa, name='ajax_load_grupa'),
]


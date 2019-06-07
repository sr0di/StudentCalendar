from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import (
    register, ProfileUpdateView,
    load_limba_predare, login_view,
    logout_request,
    load_an, load_grupa,
    delete_profil)

app_name = 'accounts'
urlpatterns = [
    path(r'register/', register, name='register'),
    path(r'login/', login_view, name="login_view"),
    path(r'logout/', logout_request, name='logout'),
    path(r'profil/', login_required(ProfileUpdateView.as_view()), name='profil_change'),
    path(r'delete_profil/', delete_profil, name='delete_profil'),
    # path(r'profil<int:pk>/', ProfileDetailView.as_view(), name='profil_detail'),



    path('ajax/load-lb/', load_limba_predare, name='ajax_load_lb'),
    path('ajax/load-an/', load_an, name='ajax_load_an'),
    path('ajax/load-grupa/', load_grupa, name='ajax_load_grupa'),
]


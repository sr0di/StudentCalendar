from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfilForm

from django.views.generic import UpdateView
from django.urls import reverse_lazy, reverse
from .models import Profil, LimbaPredare, An, Grupa


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            profil = Profil.objects.filter(user_id=form.instance.id).first()
            return redirect(reverse('profil_change', kwargs={'pk': profil.id}))
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/calendar')
        else:
            return redirect('/')
    return render(request, 'accounts/login.html')





'''
class ProfileListView(ListView):
    model = Profil
    context_object_name = 'profiles'


class ProfileCreateView(CreateView):
    model = Profil
    form_class = ProfilForm
    # fields = ('specializare', 'limba_predare', 'an', 'grupa')
    success_url = reverse_lazy('profil_changelist')
'''


class ProfileUpdateView(UpdateView):
    model = Profil
    form_class = ProfilForm
    # fields = ('specializare', 'limba_predare', 'an', 'grupa')
    success_url = reverse_lazy('planner')


def load_limba_predare(request):
    specializare_id = request.GET.get('specializare')
    limbi_predare = LimbaPredare.objects.filter(specializare_id = specializare_id).order_by('denr')
    context = {'limbi_predare': limbi_predare}
    return render(request, 'accounts/limba_predare_options.html', context)


def load_an(request):
    limba_predare_id = request.GET.get('limba_predare')
    ani = An.objects.filter(limba_predare_id=limba_predare_id).order_by('denr')
    context = {'ani': ani}
    return render(request, 'accounts/an_options.html', context)


def load_grupa(request):
    an_id = request.GET.get('an')
    grupe = Grupa.objects.filter(an_id=an_id).order_by('denr')
    context = {'grupe': grupe}
    return render(request, 'accounts/grupa_options.html', context)

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfilForm

from django.views.generic import UpdateView, DetailView
from django.urls import reverse_lazy, reverse
from .models import Profil, LimbaPredare, An, Grupa, MyUser


def index(request):
    return render(request, 'homepage.html')


def delete_profil(request):
    deletion = str(request.user.prenume)+", contul tau a fost sters!"
    MyUser.objects.get(id=request.user.id).delete()
    logout(request)
    return render(request, 'accounts/login.html', context={'deletion_massage': deletion})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data['password1']
            messages.success(request, f'Account created for {email}!')
            new_user = authenticate(request, email=email, password=password)
            login(request,  new_user)
            return redirect(reverse_lazy('accounts:profil_change'))
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
            return redirect('cal:calendar')
        else:
            error = 'Datele introduse nu sunt valide!'
            return render(request, 'accounts/login.html', context={'error': error, })
    return render(request, 'accounts/login.html')


def logout_request(request):
    logout(request)
    messages.info(request, 'Ai iesit din cont!')
    return redirect('accounts:login_view')

'''
class ProfileDetailView(DetailView):
    template_name = 'accounts/profil_detail.html'
    queryset = Profil.objects.all()
'''


class ProfileUpdateView(UpdateView):
    model = Profil
    form_class = ProfilForm
    # fields = ('specializare', 'limba_predare', 'an', 'grupa')

    def get_object(self, queryset=None):
        return self.request.user.profil

    def get_success_url(self, **kwargs):
        print(self.object.user)
        # return reverse_lazy('cal:calendar', args=(self.object.user.id,))
        return reverse_lazy('cal:calendar')


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

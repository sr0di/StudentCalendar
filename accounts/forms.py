from django import forms
from .models import MyUser, Profil, LimbaPredare, Grupa, An
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ['email', 'nume', 'prenume', 'password1', 'password2']


class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ('specializare', 'limba_predare', 'an', 'grupa')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['limba_predare'].queryset = LimbaPredare.objects.none()
        self.fields['an'].queryset = An.objects.none()
        self.fields['grupa'].queryset = Grupa.objects.none()
        print(self.instance.pk)
        # SPECIALIZARE
        if 'specializare' in self.data:
            print(self.data)
            try:
                specializare_id = int(self.data.get('specializare'))
                self.fields['limba_predare'].queryset = LimbaPredare.objects.filter(specializare_id=specializare_id).order_by('denr')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            if self.instance.specializare is not None:
                self.fields['limba_predare'].queryset = self.instance.specializare.limbi_predare.all().order_by('denr')

        # LIMBA PREDARE
        if 'limba_predare' in self.data:
            try:
                limba_predare_id = int(self.data.get('limba_predare'))
                self.fields['an'].queryset = An.objects.filter(limba_predare_id=limba_predare_id).order_by('denr')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            if self.instance.limba_predare is not None:
                self.fields['an'].queryset = self.instance.limba_predare.ani.all().order_by('denr')

        # AN
        if 'an' in self.data:
            try:
                an_id = int(self.data.get('an'))
                self.fields['grupa'].queryset = Grupa.objects.filter(an_id=an_id).order_by('denr')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            if self.instance.an is not None:
                self.fields['grupa'].queryset = self.instance.an.grupe.all().order_by('denr')

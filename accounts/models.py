from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.signals import post_save
from django.dispatch import receiver

from cal.models import Repart


class MyUserManager(BaseUserManager):

    def create_user(self, email, nume, prenume, password=None):

        if not email:
            raise ValueError('Utilizatorii trebuie sa aiba o adresa de email')

        user = self.model(
            email=self.normalize_email(email),
            nume=nume,
            prenume=prenume,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nume, prenume, password):
        user = self.create_user(
            email,
            password=password,
            nume=nume,
            prenume=prenume,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='adresa de email',
                              max_length=255,
                              unique=True,)
    nume = models.CharField(max_length=25, blank=False)
    prenume = models.CharField(max_length=25, blank=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nume', 'prenume']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Does the user have a specific permission?
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        # Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profil = Profil.objects.create(user=instance)
        profil.save()


post_save.connect(create_profile, sender=MyUser)


class Specializare(models.Model):
    denr = models.CharField(max_length=50)

    def __str__(self):
        return self.denr


class LimbaPredare(models.Model):
    structura = models.ForeignKey
    specializare = models.ForeignKey(Specializare, on_delete=models.CASCADE, related_name='limbi_predare')
    denr = models.CharField(max_length=8)
    
    def __str__(self):
        return self.denr + ',' + self.specializare.__str__()
    

class An(models.Model):
    limba_predare = models.ForeignKey(LimbaPredare, on_delete=models.CASCADE, related_name='ani')
    denr = models.IntegerField(choices=((1,'I'),(2,'II'),(3,'III')))
    
    def __str__(self):
        return str(self.denr)+','+self.limba_predare.__str__()


class Grupa(models.Model):
    an = models.ForeignKey(An, on_delete=models.CASCADE, related_name='grupe')
    denr = models.CharField(max_length=5)
    
    def __str__(self):
        return self.denr


class Profil(models.Model):
    user = models.OneToOneField('MyUser', on_delete=models.CASCADE, related_name='profil')
    universitate = models.CharField(max_length=26, default='Universitatea Babeș-Bolyai', editable=False)
    facultate = models.CharField(max_length=39, default='Facultatea de Matematică și Informatică', editable=False)
    specializare = models.ForeignKey(Specializare, on_delete=models.SET_NULL, null=True)
    limba_predare = models.ForeignKey(LimbaPredare, on_delete=models.SET_NULL, null=True)
    an = models.ForeignKey(An, on_delete=models.SET_NULL, null=True)
    grupa = models.ForeignKey(Grupa, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.__str__()+', '+self.grupa.__str__()


class Activitate(models.Model):
    profil = models.ForeignKey('Profil', on_delete=models.CASCADE, related_name="activitati")
    disciplina = models.ForeignKey('cal.Repart', on_delete=models.CASCADE)
    hidden = models.BooleanField(default=False)


@receiver(post_save, sender=Profil)
def create_orar(sender, instance, created, **kwargs):
    if not created:
        if instance.grupa is not None:
            activitati = Repart.objects.filter(formatie__componenta__contains=instance.grupa)
            Activitate.objects.filter(profil=instance).delete()
            if activitati.exists():
                for activitate in activitati.iterator():
                    Activitate.objects.create(profil=instance, disciplina=activitate)
                

post_save.connect(create_orar, sender=Profil)


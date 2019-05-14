from django.db import models
from .constants import TipActivitateDisciplina


class Repart(models.Model):
    frecventa = models.IntegerField(default=0, choices=((0, 'saptamanal'), (1, 'saptamana 1'), (2, 'saptamana 2')))
    semestru = models.ForeignKey('Semestru', on_delete=models.CASCADE)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)
    formatie = models.ForeignKey('Formatie', on_delete=models.CASCADE)
    cadru = models.ForeignKey('Cadru', on_delete=models.CASCADE)
    sala = models.ForeignKey('Sala', on_delete=models.CASCADE)
    zi = models.ForeignKey('Zi', on_delete=models.CASCADE)
    tip_activitate = models.CharField(max_length=1, choices=TipActivitateDisciplina.CHOICES)
    nr_ore = models.IntegerField(blank=True)
    ora_i = models.IntegerField(null=False)
    ora_s = models.IntegerField(null=False)


class Semestru(models.Model):
    numar = models.IntegerField(choices=((1, 'I'), (2, 'II')))
    tip_an = models.CharField(default='NT', blank=True, max_length=10, choices=(('NT', 'Neterminal'), ('T', 'Terminal')))
    numar_saptamani = models.IntegerField(default=14, choices=((14, '14 săptămâni'), (12, '12 săptămâni')))
    data_inceput = models.DateField()
    data_sfarsit = models.DateField()

    def __str__(self):
        return str(self.numar)+', '+str(self.tip_an)


class Cadru(models.Model):
    nume = models.CharField(max_length=30, null=False)
    web = models.CharField(max_length=50, blank=True, default='')
    catedra = models.ForeignKey('Catedra', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    activ = models.IntegerField(default=1)  # by default is active
    cod = models.CharField(max_length=5)

    def __str__(self):
        return self.nume


class Sala(models.Model):
    cod = models.CharField(max_length=10, null=False)
    legenda = models.CharField(max_length=80, default='')
    cladire = models.ForeignKey('Cladire',on_delete=models.CASCADE)

    def __str__(self):
        return self.cod


class Cladire(models.Model):
    denr = models.CharField(max_length=40, null=False)
    descriere = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.denr


class Zi(models.Model):
    cod = models.IntegerField(null=False)
    denr = models.CharField(max_length=8, null=False)

    def __str__(self):
        return str(self.cod)


class Formatie(models.Model):
    an = models.IntegerField()
    cod = models.CharField(max_length=10, null=False)
    denumire = models.CharField(max_length=20, blank=True)
    nivel = models.IntegerField()
    componenta = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.cod


class Disciplina(models.Model):
    cod = models.CharField(max_length=10, null=False, default='')
    denr = models.CharField(max_length=120, null=False)

    def __str__(self):
        return self.denr


class Catedra(models.Model):
    denr = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.denr


class Post(models.Model):
    nume = models.CharField(max_length=20, null=False, default='')
    denr = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.denr

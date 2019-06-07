from django.contrib import admin
from .models import Repart, Cadru, Catedra, Cladire, Zi, Semestru, Sala, Formatie, Disciplina, Post, \
    ActivitateNedidactica, StructuraSemestru


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'nume', 'denr']


class CatedraAdmin(admin.ModelAdmin):
    list_display = ['id', 'denr']


class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cod', 'denr']


class FormatieAdmin(admin.ModelAdmin):
    list_display = ['id', 'an', 'cod', 'denumire', 'nivel', 'componenta']


class ZiAdmin(admin.ModelAdmin):
    list_display = ['id', 'cod', 'denr']


class CladireAdmin(admin.ModelAdmin):
    list_display = ['id', 'denr', 'descriere']


class SalaAdmin(admin.ModelAdmin):
    list_display = ['id', 'cod', 'legenda', 'cladire']


class CadruAdmin(admin.ModelAdmin):
    list_display = ['id', 'nume', 'web', 'catedra', 'post', 'activ', 'cod']


class SemestruAdmin(admin.ModelAdmin):
    list_display = ['id', 'numar', 'tip_an', 'numar_saptamani', 'data_inceput', 'data_sfarsit']


class RepartAdmin(admin.ModelAdmin):
    list_display = ['id', 'semestru', 'disciplina', 'formatie', 'cadru', 'sala', 'zi', 'tip_activitate', 'nr_ore', 'ora_i', 'ora_s']


class ActivitateNedidacticaAdmin(admin.ModelAdmin):
    list_display = ['id', 'structura', 'data_inceput', 'data_sfarsit', 'descriere']


class StructuraSemestruAdmin(admin.ModelAdmin):
    list_display = ['id', 'semestru', 'get_limbi_predare', 'descriere']


admin.site.register(ActivitateNedidactica, ActivitateNedidacticaAdmin)
admin.site.register(StructuraSemestru, StructuraSemestruAdmin)
admin.site.register(Repart, RepartAdmin)
admin.site.register(Semestru, SemestruAdmin)
admin.site.register(Cadru, CadruAdmin)
admin.site.register(Sala, SalaAdmin)
admin.site.register(Cladire, CladireAdmin)
admin.site.register(Zi, ZiAdmin)
admin.site.register(Formatie, FormatieAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Catedra, CatedraAdmin)
admin.site.register(Post, PostAdmin)

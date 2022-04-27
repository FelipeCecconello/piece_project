from django.contrib import admin
from .models import Membro, Bando, AkumaNoMi

class ListandoMembros(admin.ModelAdmin):
    list_display = ('id', 'nome_membro')

class ListandoBandos(admin.ModelAdmin):
    list_display = ('id', 'nome_bando')

class ListandoAkumas(admin.ModelAdmin):
    list_display = ('id', 'nome_fruta')

admin.site.register(Membro, ListandoMembros)
admin.site.register(Bando, ListandoBandos)
admin.site.register(AkumaNoMi, ListandoAkumas)


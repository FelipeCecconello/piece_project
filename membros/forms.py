from django import forms
from .models import Bando, AkumaNoMi, Membro
from datetime import datetime

class MembroForm(forms.ModelForm):
    class Meta:
        model = Membro
        fields = ['nome_membro', 'função', 'bando', 'akuma_no_mi', 'foto_membro', 'data_membro']

class BandoForm(forms.ModelForm):
    class Meta:
        model = Bando
        fields = ['nome_bando', 'quantidade_membros', 'foto_bando']

class AkumaForm(forms.ModelForm):
    class Meta:
        model = AkumaNoMi
        fields = ['nome_fruta', 'categoria', 'foto_akuma']
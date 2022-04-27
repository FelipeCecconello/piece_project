from django.db import models
from datetime import datetime
from django.forms import ModelForm
from django import forms
from django.forms.models import BaseModelFormSet

class Bando(models.Model):
    nome_bando = models.CharField(max_length=100)
    quantidade_membros = models.IntegerField()
    foto_bando = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)

    def __str__(self):
        return self.nome_bando

class AkumaNoMi(models.Model):
    CATEGORY_CHOICES = (
        ('Logia', 'Logia'),
        ('Paramecia', 'Paramecia'),
        ('Zoan', 'Zoan'),
    )

    nome_fruta = models.CharField(max_length=100)
    categoria = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    foto_akuma = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)

    def __str__(self):
        return self.nome_fruta

class Membro(models.Model):
    nome_membro = models.CharField(max_length=100)
    bando = models.ForeignKey(Bando, on_delete=models.CASCADE)
    função = models.CharField(max_length=200)
    akuma_no_mi = models.OneToOneField(AkumaNoMi, on_delete=models.CASCADE)
    foto_membro = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True)
    data_membro = models.DateTimeField(default=datetime.now, blank=True)

class BaseBandoFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        kwargs['queryset'] = Bando.objects.none()
        super(BaseBandoFormSet, self).__init__(*args, **kwargs)

class BaseAkumaFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        kwargs['queryset'] = AkumaNoMi.objects.none()
        super(BaseAkumaFormSet, self).__init__(*args, **kwargs)

class BaseMembroFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        kwargs['queryset'] = Membro.objects.none()
        super(BaseMembroFormSet, self).__init__(*args, **kwargs)

class EditMembroFormSet(BaseModelFormSet):
    def __init__(self, instance, *args, **kwargs):
        super().__init__(instance, *args, **kwargs)
        self.queryset = Membro.objects.get(pk=instance.id)


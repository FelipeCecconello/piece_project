from django.shortcuts import render, get_object_or_404, redirect
from .models import Membro, Bando, AkumaNoMi, BaseMembroFormSet, BaseAkumaFormSet, BaseBandoFormSet
from .forms import MembroForm, AkumaForm, BandoForm
from django.forms.models import modelformset_factory

# Create your views here.
def index(request):

    membros = Membro.objects.all()

    dados = {
        'membros' : membros
    }
    return render(request,'index.html', dados)

def membro(request, membro_id):
    membro = get_object_or_404(Membro, pk=membro_id)

    membro_a_exibir = {
        'membro' : membro
    }
    return render(request, 'membro.html', membro_a_exibir)

def cria_membro(request):
    MembroFormSet = modelformset_factory(Membro, fields=('nome_membro', 'bando', 'função', 'akuma_no_mi', 'foto_membro', 'data_membro'), formset=BaseMembroFormSet)
    if request.method == 'POST':
        formset = MembroFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect('index')
    else:
        formset = MembroFormSet()
    return render(request, 'cria_membro.html', {
        'formset': formset,
    })

def bandos(request):
    bandos = Bando.objects.all()

    dados = {
        'bandos': bandos
    }
    return render(request, 'bandos.html', dados)

def bando(request, bando_id):
    bando = get_object_or_404(Bando, pk=bando_id)

    bando_a_exibir = {
        'bando': bando
    }
    return render(request, 'bando.html', bando_a_exibir)

def cria_bando(request):
    BandoFormSet = modelformset_factory(Bando, fields=('nome_bando', 'quantidade_membros', 'foto_bando'), formset=BaseBandoFormSet)
    if request.method == 'POST':
        formset = BandoFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect('bandos')
    else:
        formset = BandoFormSet()
    return render(request, 'cria_bando.html', {
        'formset':formset,
    })

def akumas(request):
    akumas = AkumaNoMi.objects.all()

    dados = {
        'akumas': akumas
    }
    return render(request, 'akumas.html', dados)

def akuma(request, akuma_id):
    akuma = get_object_or_404(AkumaNoMi, pk=akuma_id)

    akuma_a_exibir = {
        'akuma': akuma
    }
    return render(request, 'akuma.html', akuma_a_exibir)

def cria_akuma(request):
    AkumaFormSet = modelformset_factory(AkumaNoMi, fields=('nome_fruta', 'categoria', 'foto_akuma'), formset=BaseAkumaFormSet)
    if request.method == 'POST':
        formset = AkumaFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect('akumas')
    else:
        formset = AkumaFormSet()
    return render(request, 'cria_akuma.html', {
        'formset': formset,
    })

def deleta_membro(request, membro_id):
    Membro.objects.filter(id=membro_id).delete()
    return redirect('index')

def deleta_akuma(request, akuma_id):
    AkumaNoMi.objects.filter(id=akuma_id).delete()
    return redirect('akumas')

def deleta_bando(request, bando_id):
    Bando.objects.filter(id=bando_id).delete()
    return redirect('bandos')

def edita_membro(request, membro_id):
    membro = Membro.objects.get(pk=membro_id)
    membroForm = MembroForm(instance=membro)
    if request.method == 'POST':
        membroForm = MembroForm(request.POST, request.FILES, instance=membro)

        if membroForm.is_valid():
            membroForm.save()
            return redirect('index')
    else:
        formset = membroForm
    return render(request, 'edita_membro.html', {
        'formset': formset,
    })

def edita_bando(request, bando_id):
    bando = Bando.objects.get(pk=bando_id)
    bandoForm = BandoForm(instance=bando)
    if request.method == 'POST':
        bandoForm = BandoForm(request.POST, request.FILES, instance=bando)

        if bandoForm.is_valid():
            bandoForm.save()
            return redirect('bandos')
    else:
        formset = bandoForm
    return render(request, 'edita_bando.html', {
        'formset': formset,
    })

def edita_akuma(request, akuma_id):
    akuma = AkumaNoMi.objects.get(pk=akuma_id)
    akumaForm = AkumaForm(instance=akuma)
    if request.method == 'POST':
        akumaForm = AkumaForm(request.POST, request.FILES, instance=akuma)

        if akumaForm.is_valid():
            akumaForm.save()
            return redirect('akumas')
    else:
        formset = akumaForm
    return render(request, 'edita_akuma.html', {
        'formset': formset,
    })
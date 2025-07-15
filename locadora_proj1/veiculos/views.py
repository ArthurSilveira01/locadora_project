from django.shortcuts import render, redirect, get_object_or_404

from .forms import VeiculoForm
from .models import Automovel

# Create your views here.
def lista_automoveis(request):
    automovel = Automovel.objects.all().order_by('placa')
    return render(request,
              'veiculos/lista_automoveis.html',
              {'automovel' : automovel})

def adicionar_automovel(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('veiculos:lista_automoveis')
    else:
        form = VeiculoForm()
        return render(request,
                      'veiculos/adicionar_automovel.html',
                      {'form' : form,
                      'titulo_pagina': 'Adicionar Automovel'})

def detalhe_automovel(request, pk):
    automovel = get_object_or_404(Automovel, pk)

    return render(request, 'veiculos/detalhe_automovel.html', {'automovel' : automovel})

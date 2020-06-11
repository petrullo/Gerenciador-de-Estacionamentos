from django.shortcuts import render
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista,
)

def home(request):
    context = {'mensagem': 'Olá'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html',{'pessoas':pessoas})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html',{'veiculos':veiculos})


def lista_movrotativos(request):
    movrot = MovRotativo.objects.all()
    return render(request, 'core/lista_movrotativos.html',{'movrot':movrot})


def lista_mensalistas(request):
    mensalista = Mensalista.objects.all()
    return render(request, 'core/lista_mensalistas.html',{'mensalista':mensalista})


def lista_movemensalistas(request):
    movmensal = MovMensalista.objects.all()
    return render(request, 'core/lista_movemensalistas.html',{'movmensal':movmensal})

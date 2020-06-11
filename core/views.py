from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {'mensagem': 'Olá'}
    return render(request, 'core/index.html', context)

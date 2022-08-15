from django.shortcuts import render

# Create your views here.

def index(request):

    receitas = {
        1: 'Lasanha',
        2: 'Sorvete',
        3: 'Pizza',
        4: 'Pudim',
        5: 'Bolo de cenoura',
        6: 'Nhoque'
    }

    dados = {
        'nome_das_receitas': receitas
    }

    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')
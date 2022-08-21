from django.shortcuts import render
from animais.models import Animal

# Create your views here.

def index(request):

    ctx = {
        'caracteristicas': None
    }

    if 'buscar' in request.GET:

        animais = Animal.objects.all()
        animal_pesquisado = request.GET['buscar']
        resultado = animais.filter(nome_animal__icontains=animal_pesquisado)

        ctx = {
            'caracteristicas': resultado
        }

    return render(request, 'index.html', ctx)

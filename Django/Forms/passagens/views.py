from ast import Pass
from django.shortcuts import render
from passagens.forms import PassagemForm, PessoaForm

# Create your views here.

def index(request):

    form = PassagemForm()
    pessoa_form = PessoaForm()

    ctx = {
        'form': form,
        'pessoa_form': pessoa_form
    }
    
    return render(request, 'index.html', ctx)

def revisao(request):

    if request.method == 'POST':

        form = PassagemForm(request.POST)
        pessoa_form = PessoaForm(request.POST)

        if form.is_valid():

            ctx = {
                'form' : form,
                'pessoa_form': pessoa_form
            }

            return render(request, 'revisao.html', ctx)
        else:

            ctx = {
                'form' : form,
                'pessoa_form': pessoa_form
            }

            return render(request, 'index.html', ctx)

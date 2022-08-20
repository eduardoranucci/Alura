from datetime import datetime
from django import forms
from tempus_dominus.widgets import DatePicker
from passagens.classe_viagem import tipos_de_classe

class PassagemForm(forms.Form):

    origem = forms.CharField(label='Origem', max_length=50)
    destino = forms.CharField(label='Destino', max_length=50)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipos_de_classe)
    informacoes = forms.CharField(
        label='Informações adicionais',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='E-mail', max_length=100)
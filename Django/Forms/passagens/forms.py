from django import forms

class PassagemForm(forms.Form):

    origem = forms.CharField(label='Origem', max_length=50)
    destino = forms.CharField(label='Destino', max_length=50)
    data_ida = forms.DateField(label='Ida')
    data_volta = forms.DateField(label='Volta')
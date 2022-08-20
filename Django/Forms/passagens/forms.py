from django import forms
from tempus_dominus.widgets import DatePicker

class PassagemForm(forms.Form):

    origem = forms.CharField(label='Origem', max_length=50)
    destino = forms.CharField(label='Destino', max_length=50)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
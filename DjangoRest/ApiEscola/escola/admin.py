from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

# Register your models here.

class Alunos(admin.ModelAdmin):

    list_display = ('id', 'nome', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'cpf')
    list_per_page = 20
    

class Cursos(admin.ModelAdmin):

    list_display = ('id', 'codigo', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo')
    search_fields = ('descricao', 'nivel')
    list_per_page = 20


class Matriculas(admin.ModelAdmin):

    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id', 'aluno')
    search_fields = ('aluno', 'curso', 'periodo')
    list_per_page = 20

admin.site.register(Aluno, Alunos)
admin.site.register(Curso, Cursos)
admin.site.register(Matricula, Matriculas)
from escola.models import Curso, Aluno
from .serializer import CursoSerializer, AlunoSerializer
from rest_framework import viewsets

# Create your views here.

class AlunosViewSet(viewsets.ModelViewSet):
    '''
    Exibe todos os alunos matriculados.
    '''

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    '''
    Exibe todos os cursos.
    '''

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


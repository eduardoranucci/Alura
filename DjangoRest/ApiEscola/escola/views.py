from escola.models import Curso, Aluno, Matricula
from .serializer import (CursoSerializer, AlunoSerializer, 
MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaMatriculasCursoSerializer)
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AlunosViewSet(viewsets.ModelViewSet):
    '''
    Exibe todos os alunos matriculados.
    '''

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    '''
    Exibe todos os cursos.
    '''

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculasViewSet(viewsets.ModelViewSet):
    '''
    Exibe todos as matrículas.
    '''

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasAlunoViewSet(generics.ListAPIView):
    '''
    Exibe as matrículas de um aluno.
    '''

    def get_queryset(self):
        
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasCursoViewSet(generics.ListAPIView):
    '''
    Exibe os alunos matriculados em um curso 
    '''

    def get_queryset(self):

        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasCursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
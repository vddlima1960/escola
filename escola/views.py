from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer
from escola.serializer import ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer

# Create your views here.

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""  #docstring
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permissions_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""  #docstring
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permissions_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matrículas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permissions_classes = [IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
    """Exibindo as matrículas de um aluno ou aluna"""  #docstring
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permissions_classes = [IsAuthenticated]


class ListaAlunosMatriculados(generics.ListAPIView):
    """Exibindo alunos e alunas matriculados em um curso"""  #docstring
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permissions_classes = [IsAuthenticated]





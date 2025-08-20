# Views receberão as requisições HTTP
# ===================================

from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

# View para listar, criar, atualizar e deletar diretores
class DirectorsView(ModelViewSet):
    # = SELECT * FROM directors
    queryset = Directors.objects.all()
    serializer_class = DirectorSerializer

# View para listar, criar, atualizar e deletar filmes
class MoviesView(ModelViewSet):
    # = SELECT * FROM movies
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

# View para listar, criar, atualizar e deletar planos
class PlansView(ModelViewSet):
    # = SELECT * FROM plans
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer

# View para listar, criar, atualizar e deletar planos
class FavoriteMovieView(ModelViewSet):
    # = SELECT * FROM plans
    queryset = FavoriteMovie.objects.all()
    serializer_class = FavoriteMoviesSerializer
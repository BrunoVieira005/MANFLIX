# Views receberá as requisições HTTP
# =================================

from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

class DirectorsView(ModelViewSet):
    # = select * from directors
    queryset = Directors.objects.all()
    serializer_class = DirectorSerializer

class MoviesView(ModelViewSet):
    # = select * from directors
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class PlansView(ModelViewSet):
    # = select * from directors
    queryset = Plans.objects.all()
    serializer_class = PlansSerializer
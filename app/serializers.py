from rest_framework import serializers

from .models import *

# Cria a classe DirectorSerializer
class DirectorSerializer(serializers.ModelSerializer):    
    #Classe de configuração
    class Meta: 
        model = Directors
        fields = '__all__'
        many = True

# Cria a classe MoviesSerializer
class MoviesSerializer(serializers.ModelSerializer):    
    #Classe de configuração
    class Meta: 
        model = Movies
        fields = '__all__'
        many = True

# Cria a classe PlansSerializer
class PlansSerializer(serializers.ModelSerializer):    
    #Classe de configuração
    class Meta: 
        model = Plans
        fields = '__all__'
        many = True
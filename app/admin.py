from django.contrib import admin
from .models import *

# Cria a classe MovieAdmin para customizar a exibição da lista de filmes e permitir pesquisa por campo de título ou categoria
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'classification')
    search_fields = ('title', 'category')
    
# Registra os modelos no site
admin.site.register(Movies, MovieAdmin)
admin.site.register(Plans)
admin.site.register(Directors)
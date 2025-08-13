from django.db import models

# Categorias definidas como tuplas para serem escolhidas

CATEGORIES = [
    ('Terror',          'Terror'),
    ('Ficção',          'Ficção'),
    ('Comédia',         'Comédia'),
    ('Documentário',    'Documentário'),
    ('Ação',            'Ação'),
    ('Suspense',        'Suspense'),
]

# Classe Diretores, para fazer o relacionamento com a classe dos filmes
class Directors(models.Model):
    name = models.CharField(max_length=400, null=False, blank=False)

    def __str__(self):
        return self.name
    
# Classe Filmes
class Movies(models.Model):
    title = models.CharField(max_length=400, null=True, blank=True)
    description = models.CharField(max_length=1000, null=False, blank=False)
    category = models.CharField(max_length=50, choices=CATEGORIES, null=False)
    published_date = models.DateField(null=False)
    photo = models.CharField(max_length=1000, null=False, blank=False)
    directors = models.ManyToManyField(Directors)
    classification = models.IntegerField()

    def __str__(self):
        return self.title

# Classe Planos
class Plans(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2) # Máximo de dígitos 6, e duas casas decimais

    def __str__(self):
        return self.name
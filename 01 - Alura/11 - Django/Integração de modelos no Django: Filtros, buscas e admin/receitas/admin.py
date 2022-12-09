from encodings import search_function
from django.contrib import admin
from .models import Receita

class ListandoReceitas(admin.ModelAdmin):
    #lista as infromação que serão mostradas nos objetos receita
    list_display = ('id','nome_receita', 'categoria','publicada')
    
    #defino o que será link na listagem
    list_display_links = ('id', 'nome_receita')

    #adciona um filtro de receitas
    search_fields = ('nome_receita',)

    #Adciona um filtro categorico
    list_filter = ('categoria',)

    #cria paginação na lista exibida
    list_per_page = 10

    #Cria uma lista editavel
    list_editable = ('publicada',)

# Register your models here.
admin.site.register(Receita, ListandoReceitas)
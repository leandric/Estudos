from django.contrib import admin
from .models import Pessoa
# Register your models here.

class ListandoPessoas(admin.ModelAdmin):
    #lista as infromação que serão mostradas nos objetos receita
    list_display = ('id','nome','email')

    #defino o que será link na listagem
    list_display_links = ('id', 'nome')

    #adciona um filtro de receitas
    search_fields = ('nome',)

    #cria paginação na lista exibida
    list_per_page = 10


admin.site.register(Pessoa, ListandoPessoas)
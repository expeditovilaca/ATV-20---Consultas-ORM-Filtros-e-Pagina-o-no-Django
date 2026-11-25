from django.contrib import admin
from .models import Desenvolvedora, Plataforma, Jogo

@admin.register(Desenvolvedora)
class DesenvolvedoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pais')
    search_fields = ('nome',)

@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'desenvolvedora', 'plataforma', 'ano_lancamento', 'genero')
    list_filter = ('desenvolvedora', 'plataforma')
    search_fields = ('nome',)
from django.contrib import admin
from musica.models import *
@admin.register(Titulo)
class TituloAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)
@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ('artista',)
    search_fields = ('artista',)
@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('genero',)
    search_fields = ('genero',)
@admin.register(Musica)
class MusicaAdmin(admin.ModelAdmin):
    search_fields = ('titulo', 'artistas',)
    list_filter = ('generos',)
    filter_horizontal = ('artistas', 'generos',)
    
    def get_artistas(self, obj):
        return ", ".join([artista.artista for artista in obj.artistas.all()])

    def get_generos(self, obj):
        return ", ".join([genero.genero for genero in obj.generos.all()])
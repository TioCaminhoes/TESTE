from django.shortcuts import render, get_object_or_404
from musica.models import *

def index(request):
    lista_musicas = Musica.objects.all()
    genero = Genero.objects.all()
    return render(request, 'index.html', {'musicas': lista_musicas, 'genero': genero})

def perfil(request, artista_id):
    artista = get_object_or_404(Artista, pk=artista_id)
    musicas = artista.musicas.all()
    return render(request, 'perfil.artista.html', {'artista': artista, 'musicas': musicas})

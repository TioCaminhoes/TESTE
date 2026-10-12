from django.db import models

class Artista(models.Model):
    artista = models.CharField(max_length=100)

    def __str__(self):
        return self.artista

    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'
        ordering = ['artista']

class Genero(models.Model):
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.genero

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ['genero']

class Titulo(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Título'
        verbose_name_plural = 'Títulos'
        ordering = ['titulo']
    
class Musica(models.Model):
    titulo = models.ForeignKey(Titulo, on_delete=models.CASCADE, related_name='musicas')
    artistas = models.ManyToManyField(Artista, related_name='musicas')
    generos = models.ManyToManyField(Genero, related_name='musicas')

    def __str__(self):
        return self.titulo.titulo

    class Meta:
        verbose_name = 'Música'
        verbose_name_plural = 'Músicas'
        ordering = ['titulo']
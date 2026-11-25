from django.db import models

class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.nome

class Plataforma(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    nome = models.CharField(max_length=150)
    desenvolvedora = models.ForeignKey(Desenvolvedora, on_delete=models.CASCADE, related_name='jogos')
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE, related_name='jogos')
    ano_lancamento = models.PositiveIntegerField()
    genero = models.CharField(max_length=80)
    capa_url = models.URLField(blank=True, help_text="URL de uma imagem de capa para compor o visual dos cards")

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
from django.db import models

class Planograma(models.Model):
    nome_planograma = models.CharField(max_length=255)
    loja = models.CharField(max_length=100)
    secao = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    atualizacao = models.DateTimeField(auto_now=True)
    previsao = models.DateField(null=True, blank=True)
    execucao = models.BooleanField(default=False)
    data_registro = models.DateField(auto_now=True)
    pdf = models.FileField(upload_to='planogramas_pdfs/')


    def __str__(self) -> str:
        return f"{self.nome_planograma} - {self.loja}"


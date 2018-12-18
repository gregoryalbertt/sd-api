from django.db import models

class Despesa(models.Model):
    codfavorecido = models.CharField(max_length=50)
    data = models.CharField(max_length=20)
    fase = models.CharField(max_length=10)
    favorecido = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)
    #comentarios =

    def __str__(self):
        return self.codfavorecido
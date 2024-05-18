from django.db import models
from datetime import datetime


class Todos(models.Model):
    titulo = models.CharField(verbose_name="Título: ", max_length=100, null=False, blank=False)
    data_criacao = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    data_entrega = models.DateTimeField(verbose_name="Data de Entrega: ",null=False, blank=False)
    data_finalizacao = models.DateTimeField(null=True)

    class Meta:
        ordering = ["data_entrega"]

    def mark_has_complete(self):
        if not self.data_finalizacao:
            self.data_finalizacao = datetime.today()
            self.save()
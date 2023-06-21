from django.db import models
from home.models import ClientModel

# Create your models here.
class AtendimentoModel(models.Model):
    client = models.ForeignKey(ClientModel, verbose_name="Cliente", on_delete=models.SET_NULL, null=True)
    data = models.DateField(verbose_name="Data")
    conheceu = models.CharField(max_length=50, null=True, blank=True)
    question1 = models.CharField(max_length=50, null=True, blank=True)
    question2 = models.CharField(max_length=50, null=True, blank=True)
    question3 = models.CharField(max_length=50, null=True, blank=True)
    question4 = models.CharField(max_length=50, null=True, blank=True)
    question5 = models.CharField(max_length=50, null=True, blank=True)
    question6a = models.BooleanField(blank=True)
    question6b = models.BooleanField(blank=True)
    question6c = models.BooleanField(blank=True)
    question6d = models.BooleanField(blank=True)
    question6e = models.BooleanField(blank=True)
    question6f = models.BooleanField(blank=True)
    question6g = models.BooleanField(blank=True)
    question6h = models.BooleanField(blank=True)
    question6i = models.BooleanField(blank=True)
    question6j = models.CharField(max_length=50, null=True, blank=True)
    question7a = models.BooleanField(blank=True)
    question7b = models.BooleanField(blank=True)
    question7c = models.BooleanField(blank=True)
    question7d = models.BooleanField(blank=True)
    question7e = models.BooleanField(blank=True)
    question7f = models.BooleanField(blank=True)
    question7g = models.BooleanField(blank=True)
    question7h = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.data} {self.client}'
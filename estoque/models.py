from django.db import models

class MarcaModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class InsumoModel(models.Model):
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    valor = models.FloatField(verbose_name='Valor', null=True, blank=True)
    quantidade = models.IntegerField(verbose_name='Quantidade', null=True, blank=True)

    def __str__(self) -> str:
        return self.descricao
    
class ItensInsumoModel(models.Model):
    insumo = models.ForeignKey(InsumoModel, verbose_name='Insumo', on_delete=models.SET_NULL, null=True)
    marca = models.ForeignKey(MarcaModel, verbose_name='Marca', on_delete=models.SET_NULL, null=True)
    valorUnitario = models.FloatField(verbose_name='Valor', null=True, blank=True)
    valorTotal = models.FloatField(verbose_name='Valor', null=True, blank=True)
    quantidade = models.IntegerField(verbose_name='Quantidade', null=True, blank=True)
    vencimento = models.DateField(verbose_name='Data de Vencimento')

    def __str__(self) -> str:
        return f'{self.insumo} - {self.marca}'
    

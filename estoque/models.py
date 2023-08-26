from django.db import models
from home.models import LocalModel
from datetime import date

CHOICES_OPERACAO = [
    ("Entrada" ,"Entrada"),
    ("Saída" ,"Saída"),
]

class MarcaModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class InsumoModel(models.Model):
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    valor = models.FloatField(verbose_name='Valor', null=True, blank=True)
    quantidade = models.IntegerField(verbose_name='Quantidade', null=True, blank=True)
    marca = models.ForeignKey(MarcaModel, verbose_name='Marca', on_delete=models.SET_NULL, null=True)
    situacao = models.BooleanField(default=True, verbose_name='Situação')

    def __str__(self) -> str:
        return self.descricao
    
class MovimentacaoInsumoModel(models.Model):
    operacao = models.CharField(max_length=10, choices=CHOICES_OPERACAO, default='Entrada', verbose_name='Operação')
    local = models.ForeignKey(LocalModel, on_delete=models.SET_NULL, null=True, verbose_name='Unidade')
    data = models.DateField(default=date.today)

class ItensInsumoModel(models.Model):
    movimentacao = models.ForeignKey(MovimentacaoInsumoModel, on_delete=models.CASCADE, null=True, blank=True)
    insumo = models.ForeignKey(InsumoModel, verbose_name='Insumo', on_delete=models.SET_NULL, null=True)
    valorUnitario = models.FloatField(verbose_name='Valor Unitario', null=True, blank=True)
    valorTotal = models.FloatField(verbose_name='Valor Total', null=True, blank=True)
    quantidade = models.IntegerField(verbose_name='Quantidade', null=True, blank=True)
    dataValidade = models.DateField(verbose_name='Data de Validade', default=date.today)
    dataEntrada = models.DateField(verbose_name='Data de Entrada', default=date.today)
    serie = models.CharField(max_length=20, blank=True, null=True, verbose_name='Serie')
    local = models.ForeignKey(LocalModel, verbose_name='Unidade', on_delete=models.SET_NULL, null=True, default='UNIDADE')

    def __str__(self) -> str:
        return f'{self.insumo}'
    


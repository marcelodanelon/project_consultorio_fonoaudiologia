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

class GrupoInsumoModel(models.Model):
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    perfis = models.CharField(max_length=50, blank=True, null=True, verbose_name='Perfis')
    controleDeCompra = models.CharField(max_length=3, choices=[("nao", "Não"),("sim", "Sim")], default=1, verbose_name='Controle de Compra')

    def __str__(self) -> str:
        return self.descricao

class InsumoModel(models.Model):
    descricao = models.CharField(max_length=50, verbose_name='Descrição')
    valor = models.CharField(max_length=15, verbose_name='Valor', null=True, blank=True, default=0.0)
    quantidade = models.CharField(max_length=15, verbose_name='Quantidade', null=True, blank=True, default=0)
    marca = models.ForeignKey(MarcaModel, verbose_name='Marca', on_delete=models.SET_NULL, null=True)
    grupoInsumo = models.ForeignKey(GrupoInsumoModel, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Grupo do Insumo')
    controle = models.CharField(max_length=10, choices=[('lote','Lote'),('quantidade','Quantidade')], default=1, verbose_name='Tipo de Controle')
    situacao = models.CharField(max_length=3, choices=[('sim','Sim'),('nao','Não')], default=1, verbose_name='Situação')

    def __str__(self) -> str:
        return self.descricao
    
class MovimentacaoInsumoModel(models.Model):
    operacao = models.CharField(max_length=10, choices=CHOICES_OPERACAO, default='Entrada', verbose_name='Operação')
    local = models.ForeignKey(LocalModel, on_delete=models.SET_NULL, null=True, verbose_name='Unidade')
    data = models.DateField(default=date.today, verbose_name='Data')

    def __str__(self) -> str:
        return f'{self.id}'

class ItensInsumoModel(models.Model):
    movimentacao = models.ForeignKey(MovimentacaoInsumoModel, on_delete=models.CASCADE, null=True)
    insumo = models.ForeignKey(InsumoModel, verbose_name='Insumo', on_delete=models.SET_NULL, null=True)
    valorUnitario = models.CharField(max_length=10, verbose_name='Valor Unitario', null=True)
    valorTotal = models.CharField(max_length=10, verbose_name='Valor Total', null=True)
    quantidade = models.IntegerField(verbose_name='Quantidade', null=True)
    dataValidade = models.DateField(verbose_name='Data de Validade', default=date.today)
    dataEntrada = models.DateField(verbose_name='Data de Entrada', default=date.today)
    serie = models.CharField(max_length=20, null=True, verbose_name='Serie/Lote')
    local = models.ForeignKey(LocalModel, verbose_name='Unidade', on_delete=models.SET_NULL, null=True, default='UNIDADE')

    def __str__(self) -> str:
        return f'{self.insumo}'
    
class ItensMovimentacaoInsumoModel(models.Model):
    movimentacao = models.ForeignKey(MovimentacaoInsumoModel, on_delete=models.CASCADE, null=True, verbose_name='Movimentação')
    insumo = models.ForeignKey(InsumoModel, verbose_name='Insumo', on_delete=models.SET_NULL, null=True)
    valorUnitario = models.CharField(max_length=10, verbose_name='Valor Unitario', null=True)
    valorCompra = models.CharField(max_length=10, verbose_name='Valor Compra', blank=True, null=True)
    valorTotal = models.CharField(max_length=10, verbose_name='Valor Total', null=True)
    quantidade = models.IntegerField(verbose_name='Quantidade', null=True)
    dataValidade = models.DateField(verbose_name='Data de Validade', default=date.today)
    dataEntrada = models.DateField(verbose_name='Data de Entrada', default=date.today)
    serie = models.CharField(max_length=20, null=True, verbose_name='Serie/Lote')
    local = models.ForeignKey(LocalModel, verbose_name='Unidade', on_delete=models.SET_NULL, null=True, default='UNIDADE')

    def __str__(self) -> str:
        return f'{self.insumo}'
    


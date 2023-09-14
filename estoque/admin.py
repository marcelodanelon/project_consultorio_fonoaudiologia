from django.contrib import admin
from estoque.models import MarcaModel, InsumoModel, ItensInsumoModel, ItensMovimentacaoInsumoModel, MovimentacaoInsumoModel

@admin.register(MarcaModel)
class MarcaAdmin(admin.ModelAdmin):
    ...

@admin.register(InsumoModel)
class InsumoAdmin(admin.ModelAdmin):
    ...

@admin.register(MovimentacaoInsumoModel)
class MovimentacaoInsumoAdmin(admin.ModelAdmin):
    ...

@admin.register(ItensInsumoModel)
class ItensInsumoAdmin(admin.ModelAdmin):
    list_display = 'movimentacao', 'id', 'insumo', 'serie', 'quantidade', 'dataEntrada', 
    ordering = '-movimentacao', 'insumo',

@admin.register(ItensMovimentacaoInsumoModel)
class ItensInsumoAdmin(admin.ModelAdmin):
    list_display = 'movimentacao', 'id', 'insumo', 'serie', 'quantidade', 'dataEntrada', 
    ordering = '-movimentacao', 'insumo',

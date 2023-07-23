from django.contrib import admin
from estoque.models import InsumoModel, ItensInsumoModel

@admin.register(InsumoModel)
class InsumoAdmin(admin.ModelAdmin):
    ...

@admin.register(ItensInsumoModel)
class ItensInsumoAdmin(admin.ModelAdmin):
    ...
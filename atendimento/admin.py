from django.contrib import admin
from atendimento.models import AtendimentoModel, AnamneseModel

@admin.register(AtendimentoModel)
class AtendimentoAdmin(admin.ModelAdmin):
    ...

@admin.register(AnamneseModel)
class AnamneseAdmin(admin.ModelAdmin):
    ...
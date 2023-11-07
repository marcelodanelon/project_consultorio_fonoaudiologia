from django.contrib import admin
from atendimento.models import AtendimentoModel, RegulagemModel, AudiometriaModel, ContatosTelefonicosModel

@admin.register(AtendimentoModel)
class AtendimentoAdmin(admin.ModelAdmin):
    ...

@admin.register(RegulagemModel)
class RegulagemAdmin(admin.ModelAdmin):
    ...

@admin.register(AudiometriaModel)
class AudiometriaAdmin(admin.ModelAdmin):
    ...

@admin.register(ContatosTelefonicosModel)
class ContatosTelefonicosAdmin(admin.ModelAdmin):
    ...
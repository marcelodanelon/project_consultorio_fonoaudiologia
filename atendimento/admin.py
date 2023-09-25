from django.contrib import admin
from atendimento.models import AtendimentoModel, AnamneseModel, AudiometriaModel, ContatosTelefonicosModel

@admin.register(AtendimentoModel)
class AtendimentoAdmin(admin.ModelAdmin):
    ...

@admin.register(AnamneseModel)
class AnamneseAdmin(admin.ModelAdmin):
    ...

@admin.register(AudiometriaModel)
class AudiometriaAdmin(admin.ModelAdmin):
    ...

@admin.register(ContatosTelefonicosModel)
class ContatosTelefonicosAdmin(admin.ModelAdmin):
    ...
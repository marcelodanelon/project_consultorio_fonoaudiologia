from django.contrib import admin
from atendimento.models import AtendimentoModel

# Register your models here.
@admin.register(AtendimentoModel)
class ClientAdmin(admin.ModelAdmin):
    ...
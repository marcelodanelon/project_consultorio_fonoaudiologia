from django.contrib import admin
from agendamento.models import AgendaModel, AgendamentoModel

# Register your models here.
@admin.register(AgendaModel)
class AgendaAdmin(admin.ModelAdmin):
    ...

@admin.register(AgendamentoModel)
class AgendamentoAdmin(admin.ModelAdmin):
    ...
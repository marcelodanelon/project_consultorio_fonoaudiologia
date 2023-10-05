from django.contrib import admin
from agendamento.models import AgendaModel

# Register your models here.
@admin.register(AgendaModel)
class AgendaAdmin(admin.ModelAdmin):
    ...
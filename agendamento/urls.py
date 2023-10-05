from django.urls import path
from agendamento.views import agenda

app_name = 'agendamento'

urlpatterns = [
    path('agendamento/', agenda.index, name='index'),

    # path('listInsumo/', insumo.listInsumo, name='listInsumo'),
    path('createAgenda/', agenda.createAgenda, name='createAgenda'),
    # path('searchInsumo/', insumo.searchInsumo, name='searchInsumo'),
    # path('<int:insumo_id>/updateInsumo/', insumo.updateInsumo, name='updateInsumo'),
]
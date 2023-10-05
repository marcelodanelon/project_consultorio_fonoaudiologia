from django.urls import path
from agendamento.views import agenda

app_name = 'agendamento'

urlpatterns = [
    path('agendamento/', agenda.index, name='index'),

    path('listAgenda/', agenda.listAgenda, name='listAgenda'),
    path('createAgenda/', agenda.createAgenda, name='createAgenda'),
    path('searchAgenda/', agenda.searchAgenda, name='searchAgenda'),
    path('<int:agenda_id>/updateAgenda/', agenda.updateAgenda, name='updateAgenda'),
]
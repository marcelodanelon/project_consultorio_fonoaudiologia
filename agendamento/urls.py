from django.urls import path
from agendamento.views import agenda, agendamento

app_name = 'agendamento'

urlpatterns = [
    path('agendamento/', agenda.index, name='index'),

    path('listAgenda/', agenda.listAgenda, name='listAgenda'),
    path('createAgenda/', agenda.createAgenda, name='createAgenda'),
    path('searchAgenda/', agenda.searchAgenda, name='searchAgenda'),
    path('<int:agenda_id>/updateAgenda/', agenda.updateAgenda, name='updateAgenda'),

    # path('listAgendamento/', agendamento.listAgendamento, name='listAgendamento'),
    path('createAgendamento/', agendamento.createAgendamento, name='createAgendamento'),
    # path('searchAgendamento/', agendamento.searchAgendamento, name='searchAgendamento'),
    # path('<int:agendamento_id>/updateAgendamento/', agendamento.updateAgendamento, name='updateAgendamento'),

    path('agendamento/getJSONdatas/', agendamento.getJSONdatas, name='getJSONdatas'),
    path('agendamento/getJSONhorarios/', agendamento.getJSONhorarios, name='getJSONhorarios'),
]
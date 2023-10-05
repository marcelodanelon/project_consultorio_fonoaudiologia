from django.urls import path
from agendamento.views import agenda

app_name = 'agendamento'

urlpatterns = [
    path('agendamento/', agenda.index, name='index'),
]
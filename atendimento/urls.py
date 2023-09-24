from django.urls import path
from atendimento.views import atendimento

app_name = 'atendimento'

urlpatterns = [
    path('atendimento/', atendimento.index ,name='index'),
    path('atendimento/atendimento/', atendimento.atendimento ,name='atendimento'),
    path('atendimento/audiometria/', atendimento.plano_cartesiano ,name='audiometria'),
    path('atendimento/historico/', atendimento.historicoAtendimento ,name='historicoAtendimento'),
]
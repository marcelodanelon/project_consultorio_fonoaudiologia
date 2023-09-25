from django.urls import path
from atendimento.views import atendimento, audiometria

app_name = 'atendimento'

urlpatterns = [
    path('atendimento/', atendimento.index ,name='index'),
    path('atendimento/atendimento/', atendimento.atendimento ,name='atendimento'),
    path('atendimento/historico/', atendimento.historicoAtendimento ,name='historicoAtendimento'),

    path('atendimento/audiometria/', audiometria.audiometria ,name='audiometria'),
    path('atendimento/listAudiometria/', audiometria.listAudiometria, name='listAudiometria'),
    path('atendimento/searchAudiometria/', audiometria.searchAudiometria, name='searchAudiometria'),
    path('atendimento/<int:audiometria_id>/updateAudiometria/', audiometria.updateAudiometria, name='updateAudiometria'),
    path('atendimento/<int:audiometria_id>/deleteAudiometria/', audiometria.deleteAudiometria, name='deleteAudiometria'),
]
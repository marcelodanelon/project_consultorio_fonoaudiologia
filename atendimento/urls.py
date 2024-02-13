from django.urls import path
from atendimento.views import atendimento, audiometria, motivos

app_name = 'atendimento'

urlpatterns = [
    path('atendimento/', atendimento.index ,name='index'),

    # path('atendimento/atendimento/', atendimento.atendimento ,name='atendimento'),
    path('atendimento/atendimento/', atendimento.atendimento ,name='atendimento'),
    path('atendimento/historico/', atendimento.historicoAtendimento ,name='historicoAtendimento'),

    path('atendimento/audiometria/', audiometria.audiometria ,name='audiometria'),
    path('atendimento/listAudiometria/', audiometria.listAudiometria, name='listAudiometria'),
    path('atendimento/searchAudiometria/', audiometria.searchAudiometria, name='searchAudiometria'),
    path('atendimento/<int:audiometria_id>/updateAudiometria/', audiometria.updateAudiometria, name='updateAudiometria'),
    path('atendimento/<int:audiometria_id>/deleteAudiometria/', audiometria.deleteAudiometria, name='deleteAudiometria'),

    path('listMotivo/', motivos.listMotivo, name='listMotivo'),
    path('createMotivo/', motivos.createMotivo, name='createMotivo'),
    path('searchMotivo/', motivos.searchMotivo, name='searchMotivo'),
    path('<int:motivo_id>/updateMotivo/', motivos.updateMotivo, name='updateMotivo'),
    path('<int:motivo_id>/deleteMotivo/', motivos.deleteMotivo, name='deleteMotivo'),

    path('atendimento/getJSONclient/', atendimento.getJSONclient, name='getJSONclient'),
    path('atendimento/download_documento_atendimento/', atendimento.download_documento_atendimento, name='download_documento_atendimento'),
    path('atendimento/download_documento_audiometria/', audiometria.download_documento_audiometria, name='download_documento_audiometria'),
]
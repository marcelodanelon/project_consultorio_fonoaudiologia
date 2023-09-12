from django.urls import path
from atendimento.views.atendimento import views

app_name = 'atendimento'

urlpatterns = [
    path('atendimento/', views.index ,name='index'),
    path('atendimento/atendimento/', views.atendimento ,name='atendimento'),
    path('atendimento/audiometria/', views.audiometria ,name='audiometria'),
    path('atendimento/historico/', views.historicoAtendimento ,name='historicoAtendimento'),
]
from django.urls import path
from home.views import client
from home.views import local
from home.views import professional

app_name = 'home'

urlpatterns = [
    path('', client.index, name='index'),

    path('listClient/', client.listClient, name='listClient'),
    path('createClient/', client.createClient, name='createClient'),
    path('searchClient/', client.searchClient, name='searchClient'),
    path('<int:client_id>/updateClient/', client.updateClient, name='updateClient'),
    path('<int:client_id>/deleteClient/', client.deleteClient, name='deleteClient'),

    path('listLocal/', local.listLocal, name='listLocal'),
    path('createLocal/', local.createLocal, name='createLocal'),
    path('searchLocal/', local.searchLocal, name='searchLocal'),
    path('<int:local_id>/updateLocal/', local.updateLocal, name='updateLocal'),
    path('<int:local_id>/deleteLocal/', local.deleteLocal, name='deleteLocal'),

    path('listProfessional/', professional.listProfessional, name='listProfessional'),
    path('createProfessional/', professional.createProfessional, name='createProfessional'),
    path('searchProfessional/', professional.searchProfessional, name='searchProfessional'),
    path('<int:professional_id>/updateProfessional/', professional.updateProfessional, name='updateProfessional'),
    path('<int:professional_id>/deleteProfessional/', professional.deleteProfessional, name='deleteProfessional'),
]
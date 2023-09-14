from django.urls import path
from home.views import client
from home.views import local
from home.views import professional
from home.views import user

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

    path('user/list/', user.listUser, name='listUser'),
    path('user/search/', user.searchUser, name='searchUser'),
    path('user/create/', user.register, name='registerUser'),
    path('<int:user_id>/user/update/', user.updateUser, name='updateUser'),
    path('user/login/', user.login_view, name='loginUser'),
    path('user/logout/', user.logout_view, name='logoutUser'),
]
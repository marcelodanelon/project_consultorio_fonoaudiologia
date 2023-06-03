from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('listClient/', views.listClient, name='listClient'),

    path('createClient/', views.createClient, name='createClient'),
    path('searchClient/', views.searchClient, name='searchClient'),
    path('<int:client_id>/updateClient/', views.updateClient, name='updateClient'),
    path('<int:client_id>/deleteClient/', views.deleteClient, name='deleteClient'),
]
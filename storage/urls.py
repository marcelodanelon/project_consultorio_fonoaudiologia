from django.urls import path
from storage.views import entrada

app_name = 'storage'

urlpatterns = [
    path('storage/', entrada.index, name='index'),
]

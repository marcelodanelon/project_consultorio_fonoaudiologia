from django.contrib import admin
from home.models import ClientModel, CityModel, StateModel, StatusModel

@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):
    ...

@admin.register(CityModel)
class CityAdmin(admin.ModelAdmin):
    ...

@admin.register(StateModel)
class StateAdmin(admin.ModelAdmin):
    ...

@admin.register(StatusModel)
class StatusAdmin(admin.ModelAdmin):
    ...
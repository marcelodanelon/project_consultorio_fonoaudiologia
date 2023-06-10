from django.contrib import admin
from home.models import ClientModel, StatusModel

@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):
    ...

@admin.register(StatusModel)
class StatusAdmin(admin.ModelAdmin):
    ...
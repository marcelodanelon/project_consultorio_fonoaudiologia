from django.contrib import admin
from home.models import ClientModel, StatusModel, LocalModel

@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):
    ...

@admin.register(StatusModel)
class StatusAdmin(admin.ModelAdmin):
    ...

@admin.register(LocalModel)
class StatusAdmin(admin.ModelAdmin):
    ...
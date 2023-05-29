from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class CityModel(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name
    
class StateModel(models.Model):
    name = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.name
    
class StatusModel(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name

class ClientModel(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Primeiro Nome')
    last_name = models.CharField(max_length=50, verbose_name='Sobrenome')
    born = models.DateField(verbose_name='Data de Nascimento')
    responsibleName = models.CharField(max_length=50, verbose_name='Responsável', null=True, blank=True)
    responsiblePhone = PhoneNumberField(verbose_name='Contato', null=True, blank=True)
    street = models.CharField(max_length=30, verbose_name='Logradouro', null=True, blank=True)
    district = models.CharField(max_length=30, verbose_name='Bairro', null=True, blank=True)
    number = models.IntegerField(verbose_name='Número', null=True, blank=True)
    city = models.ForeignKey(CityModel, on_delete=models.SET_NULL, verbose_name="Cidade", null=True, blank=True)
    state = models.ForeignKey(StateModel, on_delete=models.SET_NULL, verbose_name="UF", null=True, blank=True)
    zipcode = models.IntegerField(verbose_name='CEP', null=True, blank=True)
    complement = models.CharField(max_length=15, verbose_name='Complemento', null=True, blank=True)
    document1 = models.IntegerField(verbose_name='CPF', null=True, blank=True)
    document2 = models.IntegerField(verbose_name='RG', null=True, blank=True)
    phone1 = PhoneNumberField(verbose_name='Telefone', null=True, blank=True)
    phone2 = PhoneNumberField(verbose_name='Celular', null=True, blank=True)
    status = models.ForeignKey(StatusModel, on_delete=models.SET_NULL, verbose_name="Situação", null=True, blank=True)
    # owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
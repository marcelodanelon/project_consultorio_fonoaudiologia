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
    name = models.CharField(max_length=40, default='Ativo')

    def __str__(self) -> str:
        return self.name

class ClientModel(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Primeiro Nome')
    last_name = models.CharField(max_length=50, verbose_name='Sobrenome')
    born = models.DateField(verbose_name='Data de Nascimento')
    responsibleName = models.CharField(max_length=50, verbose_name='Responsável', blank=True)
    responsiblePhone = PhoneNumberField(verbose_name='Contato', blank=True)
    street = models.CharField(max_length=30, verbose_name='Logradouro', blank=True)
    district = models.CharField(max_length=30, verbose_name='Bairro', blank=True)
    number = models.IntegerField(verbose_name='Número', blank=True)
    city = models.ForeignKey(CityModel, on_delete=models.SET_NULL, null=True, verbose_name="Cidade", blank=True)
    state = models.ForeignKey(StateModel, on_delete=models.SET_NULL, null=True, verbose_name="UF", blank=True)
    zipcode = models.IntegerField(verbose_name='CEP', blank=True)
    complement = models.CharField(max_length=15, verbose_name='Complemento', blank=True)
    document1 = models.IntegerField(verbose_name='CPF', blank=True)
    document2 = models.IntegerField(verbose_name='RG', blank=True)
    phone1 = PhoneNumberField(verbose_name='Telefone', blank=True)
    phone2 = PhoneNumberField(verbose_name='Celular', blank=True)
    status = models.ForeignKey(StatusModel, on_delete=models.SET_NULL, null=True, verbose_name="Situação")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
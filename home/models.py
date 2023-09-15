from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from home.static.home.partials._liststates import *
from home.static.home.partials._listcities import *
    
class StatusModel(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name

class ClientModel(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Primeiro Nome')
    last_name = models.CharField(max_length=50, verbose_name='Sobrenome', blank=True, null=True)
    born = models.DateField(verbose_name='Data de Nascimento', blank=True, null=True)
    age = models.IntegerField(verbose_name='Idade', null=True, blank=True)
    responsibleName = models.CharField(max_length=50, verbose_name='Responsável', null=True, blank=True)
    responsiblePhone = models.CharField(max_length=20, verbose_name='Contato', null=True, blank=True)
    zipcode = models.CharField(max_length=8,verbose_name='CEP', null=True, blank=True)
    street = models.CharField(max_length=30, verbose_name='Logradouro', null=True, blank=True)
    district = models.CharField(max_length=30, verbose_name='Bairro', null=True, blank=True)
    number = models.IntegerField(verbose_name='Número', null=True, blank=True)
    city = models.CharField(max_length=40, choices= CHOICES_CITIES, null=True, blank=True, default='NULL')
    state = models.CharField(max_length=20, choices= CHOICES_STATES, null=True, blank=True, default='NULL')
    complement = models.CharField(max_length=15, verbose_name='Complemento', null=True, blank=True)
    document1 = models.CharField(max_length=11, verbose_name='CPF', null=True, blank=True)
    document2 = models.CharField(max_length=10,verbose_name='RG', null=True, blank=True)
    phone1 = models.CharField(max_length=20, verbose_name='Telefone', null=True, blank=True)
    phone2 = models.CharField(max_length=20, verbose_name='Celular', null=True, blank=True)
    profession = models.CharField(max_length=50, verbose_name='Profissão', null=True, blank=True)
    status = models.ForeignKey(StatusModel, on_delete=models.SET_NULL, verbose_name="Situação", null=True, blank=True, default=1)
    typeRegister = models.CharField(max_length=15, choices=[('simplificado','Simplificado'),('completo','Completo')], default=1, verbose_name='Tipo do Cadastro')
    # owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
class LocalModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome da Unidade')
    zipcode = models.IntegerField(verbose_name='CEP', null=True, blank=True)
    street = models.CharField(max_length=30, verbose_name='Logradouro', null=True, blank=True)
    district = models.CharField(max_length=30, verbose_name='Bairro', null=True, blank=True)
    number = models.IntegerField(verbose_name='Número', null=True, blank=True)
    city = models.CharField(max_length=40, choices= CHOICES_CITIES, null=True, blank=True, default='NULL')
    state = models.CharField(max_length=20, choices= CHOICES_STATES, null=True, blank=True, default='NULL')
    complement = models.CharField(max_length=15, verbose_name='Complemento', null=True, blank=True)
    phone1 = PhoneNumberField(verbose_name='Telefone', null=True, blank=True)
    phone2 = PhoneNumberField(verbose_name='Celular', null=True, blank=True)
    CNPJ = models.CharField(max_length=14, verbose_name='CNPJ', null=True, blank=True)
    status = models.ForeignKey(StatusModel, on_delete=models.SET_NULL, verbose_name="Situação", null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.name}'
    
class SpecialtyModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Especialidade')

    def __str__(self) -> str:
        return self.name
    
class ProfessionalModel(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Primeiro Nome')
    last_name = models.CharField(max_length=50, verbose_name='Sobrenome')
    born = models.DateField(verbose_name='Data de Nascimento')
    responsibleName = models.CharField(max_length=50, verbose_name='Pessoa para Recados', null=True, blank=True)
    responsiblePhone = PhoneNumberField(verbose_name='Contato', null=True, blank=True)
    zipcode = models.IntegerField(verbose_name='CEP', null=True, blank=True)
    street = models.CharField(max_length=30, verbose_name='Logradouro', null=True, blank=True)
    district = models.CharField(max_length=30, verbose_name='Bairro', null=True, blank=True)
    number = models.IntegerField(verbose_name='Número', null=True, blank=True)
    city = models.CharField(max_length=40, choices= CHOICES_CITIES, null=True, blank=True, default='NULL')
    state = models.CharField(max_length=20, choices= CHOICES_STATES, null=True, blank=True, default='NULL')
    complement = models.CharField(max_length=15, verbose_name='Complemento', null=True, blank=True)
    document1 = models.IntegerField(verbose_name='CPF', null=True, blank=True)
    document2 = models.IntegerField(verbose_name='RG', null=True, blank=True)
    phone1 = PhoneNumberField(verbose_name='Telefone', null=True, blank=True)
    phone2 = PhoneNumberField(verbose_name='Celular', null=True, blank=True)
    specialty = models.ForeignKey(SpecialtyModel, on_delete=models.SET_NULL, verbose_name="Especialidade", null=True)
    status = models.ForeignKey(StatusModel, on_delete=models.SET_NULL, verbose_name="Situação", null=True, blank=True, default=1)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
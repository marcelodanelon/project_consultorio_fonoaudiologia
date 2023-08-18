from typing import Any
from django import forms
from home.models import ClientModel, LocalModel, ProfessionalModel
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from home.static.home.partials._liststates import *
from home.static.home.partials._listcities import *

class LocalForm(forms.ModelForm):
    state = forms.ChoiceField(
        choices= CHOICES_STATES,
    )
    city = forms.ChoiceField(
        choices= CHOICES_CITIES,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['street'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['district'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['number'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['city'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['city'].label = 'Cidade'
        self.fields['state'].widget.attrs.update({
            'class':'form-control dropdown',
        })
        self.fields['state'].label = 'Estado'
        self.fields['zipcode'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['complement'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['CNPJ'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['phone1'].widget.attrs.update({
            'class':'form-control',
            'placeholder': '(00)00000-0000',
        })
        self.fields['phone2'].widget.attrs.update({
            'class':'form-control',
            'placeholder': '(00)00000-0000',
        })
        self.fields['status'].widget.attrs.update({
            'class':'form-control',
        })

    class Meta:
        model = LocalModel
        fields = ('name', 'phone1', 'phone2',
                'zipcode', 'street', 'district', 'number', 'city', 'state', 'complement',
                'CNPJ','status')

class ProfessionalForm(forms.ModelForm):
    state = forms.ChoiceField(
        choices= CHOICES_STATES,
    )
    city = forms.ChoiceField(
        choices= CHOICES_CITIES,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['last_name'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['born'].widget.attrs.update({
            'class':'form-control',
            'placeholder': 'dd/mm/yyyy',
        })
        self.fields['responsibleName'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['responsiblePhone'].widget.attrs.update({
            'class':'form-control',
            'placeholder': '(00)00000-0000',
        })
        self.fields['street'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['district'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['number'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['city'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['city'].label = 'Cidade'
        self.fields['state'].widget.attrs.update({
            'class':'form-control dropdown',
        })
        self.fields['state'].label = 'Estado'
        self.fields['zipcode'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['complement'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['document1'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['document2'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['phone1'].widget.attrs.update({
            'class':'form-control',
            'placeholder': '(00)00000-0000',
        })
        self.fields['phone2'].widget.attrs.update({
            'class':'form-control',
            'placeholder': '(00)00000-0000',
        })
        self.fields['specialty'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['status'].widget.attrs.update({
            'class':'form-control',
        })

    class Meta:
        model = ProfessionalModel
        fields = ('first_name', 'last_name', 'born', 'responsibleName', 'responsiblePhone',
                'zipcode', 'street', 'district', 'number', 'city', 'state', 'complement',
                'document1', 'document2', 'phone1', 'phone2','specialty', 'status',
                )

class ClientForm(forms.ModelForm):
    state = forms.ChoiceField(
        choices= CHOICES_STATES,
    )
    city = forms.ChoiceField(
        choices= CHOICES_CITIES,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['last_name'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['born'].widget.attrs.update({
            'class':'form-control mask-date',
            'placeholder': 'dd/mm/yyyy',
        })
        self.fields['responsibleName'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['responsiblePhone'].widget.attrs.update({
            'class':'form-control mask-telefone',
            'placeholder': '(00)00000-0000',
        })
        self.fields['street'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['district'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['number'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['city'].label = 'Cidade'
        self.fields['city'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['state'].label = 'Estado'
        self.fields['state'].widget.attrs.update({
            'class':'form-control dropdown',
        })
        self.fields['zipcode'].widget.attrs.update({
            'class':'form-control maskfm-cep',
        })
        self.fields['complement'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['document1'].widget.attrs.update({
            'class':'form-control maskfm-cpf',
        })
        self.fields['document2'].widget.attrs.update({
            'class':'form-control maskfm-rg',
        })
        self.fields['phone1'].widget.attrs.update({
            'class':'form-control mask-telefone',
            'placeholder': '(00)00000-0000',
        })
        self.fields['phone2'].widget.attrs.update({
            'class':'form-control mask-telefone',
            'placeholder': '(00)00000-0000',
        })
        self.fields['status'].widget.attrs.update({
            'class':'form-control',
        })

    class Meta:
        model = ClientModel
        fields = ('first_name', 'last_name', 'born', 'responsibleName', 'responsiblePhone',
                'zipcode', 'street', 'district', 'number', 'city', 'state', 'complement',
                'document1', 'document2', 'phone1', 'phone2','status',
                )

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=1,
        label='Primeiro nome'
        # error_messages={
        #     'required': 'Campo de preenchimento obrigatório'
        # }
    )
    last_name = forms.CharField(
        required=True,
        min_length=1,
        label='Sobrenome'
    )
    email = forms.EmailField(
        required=True,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['last_name'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['email'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['username'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['password1'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['password2'].widget.attrs.update({
            'class':'form-control',
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Um usuário com este email já existe.', code='invalid')
                )
        
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        current_username = self.instance.username

        if current_username != username:
            if User.objects.filter(email=username).exists():
                self.add_error(
                    'username',
                    ValidationError('Um usuário com este Usuário já existe.', code='invalid')
                )
        
        return username
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', ValidationError(errors))

        return password1
        
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        min_length=1,
        label='Primeiro nome'
    )
    last_name = forms.CharField(
        required=True,
        min_length=1,
        label='Sobrenome'
    )
    email = forms.EmailField(
        required=True,
    )

    password1 = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Confirmação de senha",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use a mesma senha informada no campo anterior.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['last_name'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['email'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['username'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['password1'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['password2'].widget.attrs.update({
            'class':'form-control',
        })

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)
        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não conferem!')
                )

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Um usuário com este email já existe.', code='invalid')
                )        
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        current_username = self.instance.username

        if current_username != username:
            if User.objects.filter(username=username).exists():
                self.add_error(
                    'username',
                    ValidationError('Um usuário com este Usuário já existe.', code='invalid')
                )        
        return username
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', ValidationError(errors))

        return password1
from django.shortcuts import render, redirect, get_object_or_404
from  django.urls import reverse
from home.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import Http404

def register(request):
    form_action = reverse('home:registerUser')
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Operador criado com sucesso!')

            return redirect('home:listUser')

    context = {
        'form': form,
        'form_errors': form.errors.as_text(),
        'name_module': 'Home',
        'name_screen': 'Operador',
        'title': 'Operador',
        'form_action': form_action,
    }

    return render(
        request,
        'home/register/register.html',
        context
    )

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            messages.success(request, 'Logado com sucesso!')
            user = form.get_user()
            auth.login(request, user)
            return redirect('home:index')
        else:
            messages.error(request, 'Login incorreto!')

    context = {
        'form': form,
    }

    return render(
        request,
        'home/register/login.html',
        context
    )

def logout_view(request):
    auth.logout(request)
    return redirect('home:loginUser')

def updateUser(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    form_action = reverse('home:updateUser', args=(user_id,))

    if user_id==1:
        raise Http404
    
    if request.method == 'POST':
        formUser = RegisterUpdateForm(request.POST, instance=user)

        if formUser.is_valid():
            formUser.save()
            messages.success(request, 'Operador atualizado com sucesso!')
            return redirect('home:listUser')
        # else:
        #     if "born" in formClient.errors:
        #         messages.error(request, 'Data de Nascimento inválida!')
        #     if "responsiblePhone" or "phone1" or "phone2" in formClient.errors:
        #         messages.error(request, 'Número de telefone inválido!')

        context = {
            'form': formUser,
            'title':'Cadastro',
            'name_screen': 'Atualizar',
            'option_delete': 'yes',
            'client': user,
            'form_action': form_action,
        }

        return render(
            request,
            'home/register/register.html',
            context
        )

    context = {
            'form': RegisterUpdateForm(instance=user),
            'title':'Cadastro',
            'name_screen': 'Atualizar',
            'option_delete': 'yes',
            'client': user,
            'form_action': form_action,
    }

    return render(
        request,
        'home/register/register.html',
        context
    )
from django.shortcuts import render, redirect
from home.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Operador criado com sucesso!')

            return redirect('home:index')

    context = {
        'form': form,
        'form_errors': form.errors.as_text(),
        'name_module': 'Home',
        'name_screen': 'Operador',
        'title': 'Operador',
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
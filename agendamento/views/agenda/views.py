from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required(login_url='home:loginUser')
def index(request):

    context = {
        'name_module': 'Agendamento',
    }

    return render(
        request,
        "agendamento/index.html",
        context
    )
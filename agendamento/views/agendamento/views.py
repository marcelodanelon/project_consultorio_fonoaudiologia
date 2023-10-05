from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from agendamento.models import AgendaModel

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

@login_required(login_url='home:loginUser')
def listAgenda(request):
    form_action = reverse('agendamento:createAgenda')

    agendas = AgendaModel.objects.all().order_by('id')

    paginator = Paginator(agendas, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'page_obj': page_obj,
            'title':'Cadastro',
            'name_module': 'Agendamento',
            'form_action': form_action,
    }

    return render(
        request,
        'agendamento/agenda/search.html',
        context
    )

@login_required(login_url='home:loginUser')
def searchAgenda(request):
    search_agenda = request.GET.get('q','').strip()

    if search_agenda == "":
        return redirect('agendamento:listAgenda')

    if search_agenda.isdigit():
        agendas = search_agenda.objects.filter(id=int(search_agenda)).order_by('id')

    paginator = Paginator(agendas, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Agendamento',
            'page_obj': page_obj,
    }

    return render(
        request,
        'agendamento/agenda/search.html',
        context
    )
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from agendamento.models import AgendaModel, AgendamentoModel
from home.models import ProfessionalModel, LocalModel

@login_required(login_url='home:loginUser')
def index(request):
    # Criação primeiro gráfico por Agendamento e profissional
    count = int(ProfessionalModel.objects.all().count())
    professionals = list(ProfessionalModel.objects.all())
    data_points1 = []
    for i in range(count):
        professional = AgendamentoModel.objects.filter(aProfessional=professionals[i])
        if not professional != None:
            data_points1.append({'label': 'Sem registros', "y": 0})
            break
        else:
            data_points1.append({'label': str(professional.first().aProfessional), "y": professional.count()})

    # Criação segundo gráfico por Agendamento e unidade
    count = int(LocalModel.objects.all().count())
    locais = list(LocalModel.objects.all())
    data_points2 = []
    for i in range(count):
        local = AgendamentoModel.objects.filter(aLocal=locais[i])
        if not local != None:
            data_points2.append({'label': 'Sem registros', "y": 0})
            break
        else:
            data_points2.append({'label': str(local.first().aLocal), "y": local.count()})

    context = {
        'name_module': 'Agendamento',
        'data_points' : data_points1,
        'data_points2' : data_points2,
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
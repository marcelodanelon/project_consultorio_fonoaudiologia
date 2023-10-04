from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.models import ClientModel
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator
from datetime import date

def isDate(var):
    try:
        d = datetime.strptime(var, '%d/%m/%Y').date()
        return True
    except:
        return False

@login_required(login_url='home:loginUser')
def index(request):
    # Busca de aniversariantes do dia e idade
    mes_atual=date.today().month
    data_atual=date.today().day
    aniversarios=ClientModel.objects.filter(born__day=data_atual).filter(born__month=mes_atual)
    for a in aniversarios:
        today = date.today()
        a.age = today.year - a.born.year - ((today.month, today.day) < (a.born.month, a.born.day))

    # Criação primeiro gráfico de Faixas Etarias
    data_idade = []
    data_points = []
    clients = ClientModel.objects.all()
    ## cria a lista de idades dos clientes atualmente cadastrados
    for a in clients:
        today = date.today()
        try:
            a.age = today.year - a.born.year - ((today.month, today.day) < (a.born.month, a.born.day))
        except:
            continue
        data_idade.append(a.age)
    data_idade = sorted(set(data_idade))
    count = len(data_idade)
    ## inclui um campo de idade para cada client
    for client in clients:
        today = date.today()
        try:
            client.age = today.year - client.born.year - ((today.month, today.day) < (client.born.month, client.born.day))
        except:
            continue
    ## inclui no data do gráfico, a quantidade referente a cada idade do data_idade
    for i in range(count):
        aux = 0
        for a in range(clients.count()):
            if clients[a].age == data_idade[i]:
                aux = aux + 1
        data_points.append({'label': str(data_idade[i]) + " Anos", "y": aux})

    # Criação segundo gráfico cidades
    data_points2 = []
    data_cidades = []
    for a in clients:
        if a.city != None and a.city != '-' and not a.city.isdigit():
            data_cidades.append(a.city)
    data_cidades = list(set(data_cidades))
    count = len(data_cidades)
    for i in range(count):
        clients_db = ClientModel.objects.filter(city=data_cidades[i])
        if not clients_db != None:
            data_points2.append({'label': 'Sem registros', "y": 0})
            break
        else:
            data_points2.append({'label': data_cidades[i], "y": clients_db.count()})

    # Criação terceiro gráfico clientes e sua situação
    data_points3 = []
    clients_Ativo = ClientModel.objects.filter(status=1)
    clients_Inativo = ClientModel.objects.filter(status=2)
    data_points3.append({'label': 'Ativos', "y": clients_Ativo.count()})
    data_points3.append({'label': 'Inativos', "y": clients_Inativo.count()})

    context = {
        'title': 'Home',
        'name_module': 'Home',
        'data_points' : data_points,
        'data_points2': data_points2,
        'data_points3': data_points3,
        'aniversarios': aniversarios,
    }

    return render(
        request,
        'home/index.html',
        context
    )

@login_required(login_url='home:loginUser')
def listClient(request):
    clients = ClientModel.objects.all().order_by('id')

    paginator = Paginator(clients, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Home',
            'page_obj': page_obj,
    }

    return render(
        request,
        'home/client/search.html',
        context
    )

@login_required(login_url='home:loginUser')
def searchClient(request):
    search_client = request.GET.get('q','').strip()

    if search_client == "":
        return redirect('home:listClient')

    if search_client.isdigit():
        clients = ClientModel.objects.filter(document1=int(search_client)).order_by('id')
    elif isDate(search_client):
        clients = ClientModel.objects.filter(born=datetime.strptime(search_client, '%d/%m/%Y').date()).order_by('id')
    else:        
        clients = ClientModel.objects.filter(
            Q(first_name__iexact=search_client) | 
            Q(last_name__iexact=search_client) 
        ).order_by('id')

    paginator = Paginator(clients, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Home',
            'page_obj': page_obj,
    }

    return render(
        request,
        'home/client/search.html',
        context
    )



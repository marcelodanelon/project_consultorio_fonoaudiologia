from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.models import ClientModel
from atendimento.models import AtendimentoModel, ProfessionalModel
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator

def isDate(var):
    try:
        d = datetime.strptime(var, '%d/%m/%Y').date()
        return True
    except:
        return False

@login_required(login_url='home:loginUser')
def index(request):
    data_points = [
        { "label": "apple",  "y": 10  },
        { "label": "orange", "y": 75  },
        { "label": "banana", "y": 25  },
        { "label": "mango",  "y": 30  },
        { "label": "grape",  "y": 28  }
    ]

    count = int(ProfessionalModel.objects.all().count())
    professionals = list(ProfessionalModel.objects.all())
    data_points = []
    for i in range(count):
        professional = AtendimentoModel.objects.filter(aProfessional=professionals[i])
        print(professional.first().aProfessional)
        data_points.append({'label': str(professional.first().aProfessional), "y": professional.count()})
    print(data_points)

    context = {
        'title': 'Home',
        'name_module': 'Home',
        "data_points" : data_points,
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
        'home/search.html',
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
            Q(first_name=search_client) | 
            Q(last_name=search_client)
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
        'home/search.html',
        context
    )
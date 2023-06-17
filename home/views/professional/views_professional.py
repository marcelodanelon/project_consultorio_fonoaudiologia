from django.shortcuts import render, redirect
from home.models import ProfessionalModel
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator

def isDate(var):
    try:
        d = datetime.strptime(var, '%d/%m/%Y').date()
        return True
    except:
        return False

def listProfessional(request):
    profissionais = ProfessionalModel.objects.all().order_by('id')

    paginator = Paginator(profissionais, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'page_obj': page_obj,
    }

    return render(
        request,
        'home/professional/search.html',
        context
    )

def searchProfessional(request):
    search_profissional = request.GET.get('q','').strip()

    if search_profissional == "":
        return redirect('home:listProfessional')

    if search_profissional.isdigit():
        profissionais = ProfessionalModel.objects.filter(document1=int(search_profissional)).order_by('id')
    else:        
        profissionais = ProfessionalModel.objects.filter(
            Q(name=search_profissional)
        ).order_by('id')

    paginator = Paginator(profissionais, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'page_obj': page_obj,
    }

    return render(
        request,
        'home/professional/search.html',
        context
    )
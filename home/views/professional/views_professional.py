from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='home:loginUser')
def listProfessional(request):
    profissionais = ProfessionalModel.objects.all().order_by('id')

    paginator = Paginator(profissionais, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Home',
            'page_obj': page_obj,
    }

    return render(
        request,
        'home/professional/search.html',
        context
    )

@login_required(login_url='home:loginUser')
def searchProfessional(request):
    search_profissional = request.GET.get('q','').strip()

    if search_profissional == "":
        return redirect('home:listProfessional')

    if search_profissional.isnumeric():
        profissionais = ProfessionalModel.objects.filter(id=int(search_profissional)).order_by('id')
    else:        
        profissionais = ProfessionalModel.objects.filter(
            Q(first_name__icontains=search_profissional) |
            Q(last_name__icontains=search_profissional)
        ).order_by('id')

    paginator = Paginator(profissionais, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Home',
            'page_obj': page_obj,
    }

    return render(
        request,
        'home/professional/search.html',
        context
    )
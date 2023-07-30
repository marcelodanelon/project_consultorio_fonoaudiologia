from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.models import LocalModel
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
def listLocal(request):
    locais = LocalModel.objects.all().order_by('id')

    paginator = Paginator(locais, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Home',
            'page_obj': page_obj,
    }

    return render(
        request,
        'home/local/search.html',
        context
    )

@login_required(login_url='home:loginUser')
def searchLocal(request):
    search_local = request.GET.get('q','').strip()

    if search_local == "":
        return redirect('home:listLocal')

    if search_local.isdigit():
        locais = LocalModel.objects.filter(document1=int(search_local)).order_by('id')
    else:        
        locais = LocalModel.objects.filter(
            Q(name=search_local)
        ).order_by('id')

    paginator = Paginator(locais, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Home',
            'page_obj': page_obj,
    }

    return render(
        request,
        'home/local/search.html',
        context
    )
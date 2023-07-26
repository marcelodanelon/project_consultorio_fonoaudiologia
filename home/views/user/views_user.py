from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import datetime
from django.core.paginator import Paginator

def isDate(var):
    try:
        d = datetime.strptime(var, '%d/%m/%Y').date()
        return True
    except:
        return False

def index(request):
    context = {
        'title': 'Home',
        'name_module': 'Home',
    }

    return render(
        request,
        'home/index.html',
        context
    )

def listUser(request):
    users = User.objects.all().order_by('id').exclude(id=1)

    paginator = Paginator(users, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Home',
            'page_obj': page_obj,
    }

    return render(
        request,
        'home/register/search.html',
        context
    )

def searchUser(request):
    search_user = request.GET.get('q','').strip()

    if search_user == "":
        return redirect('home:listUser')

    if search_user.isdigit():
        users = User.objects.filter(document1=int(search_user)).order_by('id')
    elif isDate(search_user):
        users = User.objects.filter(born=datetime.strptime(search_user, '%d/%m/%Y').date()).order_by('id')
    else:        
        users = User.objects.filter(
            Q(first_name=search_user) | 
            Q(last_name=search_user)
        ).order_by('id')

    paginator = Paginator(users, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Home',
            'page_obj': page_obj,
    }

    return render(
        request,
        'home/register/search.html',
        context
    )
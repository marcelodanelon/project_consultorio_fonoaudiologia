from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from estoque.models import InsumoModel
from django.core.paginator import Paginator

@login_required(login_url='home:loginUser')
def index(request):
    context = {
        'name_module': 'Estoque',
        'title': 'Estoque',
    }

    return render(
        request,
        'estoque/index.html',
        context
    )

@login_required(login_url='home:loginUser')
def listInsumo(request):
    form_action = reverse('estoque:createInsumo')

    insumos = InsumoModel.objects.all().order_by('id')

    paginator = Paginator(insumos, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'page_obj': page_obj,
            'title':'Cadastro',
            'name_screen': 'Cadastro',
            'name_module': 'Estoque',
            'form_action': form_action,
    }

    return render(
        request,
        'estoque/insumo/search.html',
        context
    )

@login_required(login_url='home:loginUser')
def searchInsumo(request):
    search_insumo = request.GET.get('q','').strip()

    if search_insumo == "":
        return redirect('estoque:listInsumo')

    if search_insumo.isdigit():
        insumos = InsumoModel.objects.filter(id=int(search_insumo)).order_by('id')

    paginator = Paginator(insumos, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Estoque',
            'page_obj': page_obj,
    }

    return render(
        request,
        'estoque/search.html',
        context
    )
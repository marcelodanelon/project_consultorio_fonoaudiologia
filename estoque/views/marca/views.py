from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from estoque.models import MarcaModel
from django.core.paginator import Paginator

@login_required(login_url='home:loginUser')
def listMarca(request):
    form_action = reverse('estoque:createMarca')

    marcas = MarcaModel.objects.all().order_by('id')

    paginator = Paginator(marcas, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'page_obj': page_obj,
            'title':'Cadastro',
            'name_module': 'Estoque',
            'form_action': form_action,
    }

    return render(
        request,
        'estoque/marca/search.html',
        context
    )

@login_required(login_url='home:loginUser')
def searchMarca(request):
    search_marca = request.GET.get('q','').strip()

    if search_marca == "":
        return redirect('estoque:listMarca')

    if search_marca.isnumeric():
        marcas = MarcaModel.objects.filter(id=int(search_marca)).order_by('id')
    else:
        marcas = MarcaModel.objects.filter(name__icontains=search_marca).order_by('id')

    paginator = Paginator(marcas, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Estoque',
            'page_obj': page_obj,
    }

    return render(
        request,
        'estoque/marca/search.html',
        context
    )
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from estoque.models import GrupoInsumoModel
from django.core.paginator import Paginator

@login_required(login_url='home:loginUser')
def listGrupo(request):
    form_action = reverse('estoque:createGrupo')

    grupos = GrupoInsumoModel.objects.all().order_by('id')

    paginator = Paginator(grupos, 14)
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
        'estoque/grupo/search.html',
        context
    )

@login_required(login_url='home:loginUser')
def searchGrupo(request):
    search_grupo = request.GET.get('q','').strip()

    if search_grupo == "":
        return redirect('estoque:listInsumo')

    if search_grupo.isdigit():
        grupos = GrupoInsumoModel.objects.filter(id=int(search_grupo)).order_by('id')

    paginator = Paginator(grupos, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Estoque',
            'page_obj': page_obj,
    }

    return render(
        request,
        'estoque/grupo/search.html',
        context
    )
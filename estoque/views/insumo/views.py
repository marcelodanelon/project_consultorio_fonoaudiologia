from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from estoque.models import InsumoModel, ItensInsumoModel
from django.core.paginator import Paginator
from django.db.models import Sum
from django.contrib import messages

@login_required(login_url='home:loginUser')
def index(request):
    items_agrupados = ItensInsumoModel.objects.values('insumo__descricao', 'local__name').annotate(total_quantidade=Sum('quantidade')).filter(total_quantidade__gt=0)
    # for item in items_agrupados:
    #     print(f'insumo: {item["insumo__descricao"]} - local: {item["local__name"]} - quantidade: {item["total_quantidade"]}')
    
    text_estoqueMin = ""
    insumos = InsumoModel.objects.exclude(quantidadeMin=None)
    for insumo in insumos:
        for item in items_agrupados:
            if insumo.descricao == item["insumo__descricao"]:
                if int(item["total_quantidade"]) < int(insumo.quantidadeMin):
                    text_estoqueMin += (f'<p>- {item["insumo__descricao"]} abaixo da quantidade minima ({insumo.quantidadeMin}) na unidade: {item["local__name"]}</p>')
    messages.info(request, text_estoqueMin)

    context = {
        'name_module': 'Estoque',
        'title': 'Estoque',
        'text_estoqueMin': text_estoqueMin,
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
        'estoque/insumo/search.html',
        context
    )
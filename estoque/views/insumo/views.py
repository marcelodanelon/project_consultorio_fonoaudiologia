from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from estoque.models import InsumoModel, ItensInsumoModel, ItensMovimentacaoInsumoModel
from home.models import LocalModel
from django.core.paginator import Paginator
from django.db.models import Sum, Avg
from datetime import date
from django.db.models import F
from django.db.models.functions import TruncDay

@login_required(login_url='home:loginUser')
def index(request):
    # controle de alerta para estoque minimo
    items_agrupados = ItensInsumoModel.objects.values('insumo__descricao', 'local__name').annotate(total_quantidade=Sum('quantidade')).filter(total_quantidade__gt=0)

    text_estoqueMin = []
    insumos = InsumoModel.objects.exclude(quantidadeMin=None)

    for insumo in insumos:
        for item in items_agrupados:
            if insumo.descricao == item["insumo__descricao"]:
                if int(item["total_quantidade"]) < int(insumo.quantidadeMin):
                    text_estoqueMin.append({
                        'descricao': item["insumo__descricao"],
                        'quantidade': item["total_quantidade"],
                        'quantidadeMin': insumo.quantidadeMin,
                        'local': item["local__name"],
                    })

    # Criação primeiro gráfico por vendas de aparelhos
    count = int(LocalModel.objects.all().count())
    locais = list(LocalModel.objects.all())
    data_points1 = []
    for i in range(count):
        local = ItensMovimentacaoInsumoModel.objects.filter(local=locais[i]).filter(insumo__grupoInsumo=1).filter(movimentacao__operacao='Saída').filter(movimentacao__data__year=date.today().year).filter(movimentacao__data__month=date.today().month)
        if not local.exists():
            data_points1.append({'label': 'Sem registros', "y": 0})
            break
        else:
            total_quantidade = local.aggregate(Sum('quantidade'))['quantidade__sum']
            data_points1.append({'label': str(local.first().local), "y": total_quantidade})

    # Criação segundo gráfico por vendas de baterias
    count = int(LocalModel.objects.all().count())
    locais = list(LocalModel.objects.all())
    data_points2 = []
    for i in range(count):
        local = ItensMovimentacaoInsumoModel.objects.filter(local=locais[i]).filter(insumo__grupoInsumo=3).filter(movimentacao__operacao='Saída').filter(movimentacao__data__year=date.today().year).filter(movimentacao__data__month=date.today().month)
        if not local.exists():
            data_points2.append({'label': 'Sem registros', "y": 0})
            break
        else:
            total_quantidade = local.aggregate(Sum('quantidade'))['quantidade__sum']
            data_points2.append({'label': str(local.first().local), "y": total_quantidade})


    # Criação terceiro gráfico itens de entrada para o mês atual / consumo médio
    data_points3 = []
    data_points4 = []
    ## ENTRADA
    itens = ItensMovimentacaoInsumoModel.objects.filter(
        dataEntrada__month=date.today().month,
        movimentacao__operacao='Entrada'
    ).annotate(dia=TruncDay('dataEntrada'))

    consumo_diario = itens.values('insumo__descricao', 'dia').annotate(total_quantidade=Sum('quantidade'))
    consumo_medio_por_insumo = {}

    for consumo in consumo_diario:
        insumo_descricao = consumo['insumo__descricao']
        total_quantidade = consumo['total_quantidade']
        
        if insumo_descricao not in consumo_medio_por_insumo:
            consumo_medio_por_insumo[insumo_descricao] = {'dias': 0, 'total_quantidade': 0}
        
        consumo_medio_por_insumo[insumo_descricao]['dias'] += 1
        consumo_medio_por_insumo[insumo_descricao]['total_quantidade'] += total_quantidade
    ### até esta parte estou agrupando para quantos dias(movimentações de entrada) esse insumo teve e qual a somatoria da quantidade desses dias
    for insumo_descricao, consumo in consumo_medio_por_insumo.items():
        dias = consumo['dias']
        total_quantidade = consumo['total_quantidade']
        consumo_medio = total_quantidade / dias
        if not insumo_descricao != None:
            data_points3.append({'label': 'Sem registros', "y": 0})
            break
        else:
            data_points3.append({'label': insumo_descricao, "y": consumo_medio})
    ### nesse parte acima, estou calculando e adicionando os dados para o meu gráfico

    ## SAIDA
    itens = ItensMovimentacaoInsumoModel.objects.filter(
        dataEntrada__month=date.today().month,
        movimentacao__operacao='Saída'
    ).annotate(dia=TruncDay('dataEntrada'))

    consumo_diario = itens.values('insumo__descricao', 'dia').annotate(total_quantidade=Sum('quantidade'))
    consumo_medio_por_insumo = {}

    for consumo in consumo_diario:
        insumo_descricao = consumo['insumo__descricao']
        total_quantidade = consumo['total_quantidade']
        
        if insumo_descricao not in consumo_medio_por_insumo:
            consumo_medio_por_insumo[insumo_descricao] = {'dias': 0, 'total_quantidade': 0}
        
        consumo_medio_por_insumo[insumo_descricao]['dias'] += 1
        consumo_medio_por_insumo[insumo_descricao]['total_quantidade'] += total_quantidade

    for insumo_descricao, consumo in consumo_medio_por_insumo.items():
        dias = consumo['dias']
        total_quantidade = consumo['total_quantidade']
        consumo_medio = total_quantidade / dias
        if not insumo_descricao != None:
            data_points4.append({'label': 'Sem registros', "y": 0})
            break
        else:
            data_points4.append({'label': insumo_descricao, "y": consumo_medio})    

    context = {
        'name_module': 'Estoque',
        'title': 'Estoque',
        'data_points':data_points1,
        'data_points2': data_points2,
        'data_points3':data_points3,
        'data_points4': data_points4,
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
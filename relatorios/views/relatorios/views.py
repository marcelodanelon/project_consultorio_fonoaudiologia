from django.shortcuts import render
from estoque.models import ItensMovimentacaoInsumoModel

def lista_itens_movimentacao(request):
    filtro_insumo = request.GET.get('filtro_insumo', '')
    filtro_valor_unitario = request.GET.get('filtro_valor_unitario', '')
    filtro_valor_total = request.GET.get('filtro_valor_total', '')
    filtro_quantidade = request.GET.get('filtro_quantidade', '')
    filtro_data_validade = request.GET.get('filtro_data_validade', '')
    filtro_data_entrada = request.GET.get('filtro_data_entrada', '')
    filtro_serie = request.GET.get('filtro_serie', '')
    filtro_local = request.GET.get('filtro_local', '')

    itens_movimentacao = ItensMovimentacaoInsumoModel.objects.all()
    
    if filtro_insumo:
        itens_movimentacao = itens_movimentacao.filter(insumo__descricao__icontains=filtro_insumo)
    if filtro_valor_unitario:
        itens_movimentacao = itens_movimentacao.filter(valorUnitario__icontains=filtro_valor_unitario)
    if filtro_valor_total:
        itens_movimentacao = itens_movimentacao.filter(valorTotal=filtro_valor_total)
    if filtro_quantidade:
        itens_movimentacao = itens_movimentacao.filter(quantidade=filtro_quantidade)
    if filtro_data_validade:
        itens_movimentacao = itens_movimentacao.filter(dataValidade=filtro_data_validade)
    if filtro_data_entrada:
        itens_movimentacao = itens_movimentacao.filter(dataEntrada=filtro_data_entrada)
    if filtro_serie:
        itens_movimentacao = itens_movimentacao.filter(serie=filtro_serie)
    if filtro_local:
        itens_movimentacao = itens_movimentacao.filter(local__name__icontains=filtro_local)

    return render(request, 'relatorios/index.html', {
        'itens_movimentacao': itens_movimentacao,
        'filtro_insumo': filtro_insumo,
        'filtro_valor_unitario': filtro_valor_unitario,
        'filtro_valor_total': filtro_valor_total,
        'filtro_quantidade': filtro_quantidade,
        'filtro_data_validade': filtro_data_validade,
        'filtro_data_entrada': filtro_data_entrada,
        'filtro_serie': filtro_serie,
        'filtro_local': filtro_local,
        'count_itens_movimentacao': itens_movimentacao.count(),
    })
# for obj in dados:
#     agrupamento = tuple(getattr(obj, campo) for campo in campos_agrupamento_selecionados)
#     if agrupamento not in dados_agrupados:
#         dados_agrupados[agrupamento] = []
#     dados_agrupados[agrupamento].append(obj)

from django.db.models import Q
from django.shortcuts import render
from relatorios.forms import RelatorioForm

def sua_view_de_relatorio_pdf(request):
    form = RelatorioForm()

    if request.method == 'POST':
        form = RelatorioForm(request.POST)
        if form.is_valid():
            campos_agrupamento_selecionados = form.cleaned_data['campos_agrupamento']
            campos_selecionados = form.cleaned_data['campos']
            resultados = ItensMovimentacaoInsumoModel.objects.all()
            
            # [FILTRO]
            # coletando todos os filtros enviados para um dict
            primeiro_filtro = {form.cleaned_data['campo_filtro']:form.cleaned_data.get('filtro_valor', None)}
            campos_filtro = {}
            for key, value in request.POST.items():
                if key.startswith('campo_filtro_'):
                    filtro_number = key.split('_')[-1] 
                    campo_name = f'filtro_valor_{filtro_number}'
                    campos_filtro[value] = request.POST[campo_name]
            campos_filtro.update(primeiro_filtro) 
                            
            # utilizando os filtros para buscar os dados
            query = Q()
            for campo, valor in campos_filtro.items():
                query &= Q(**{campo: valor})
            for campo, valor in campos_filtro.items():
                if valor:
                    resultados = ItensMovimentacaoInsumoModel.objects.filter(query)
                    break
            
            # [DETALHES]
            resultados = resultados.values(*campos_selecionados)

            context = {
                'form': form, 
                'campos_agrupamento_selecionados':campos_agrupamento_selecionados,
                'campos_selecionados':campos_selecionados,
                'resultados': resultados,
            }

            return render(
                request, 
                'relatorios/relatorio.html', 
                context,
            )

    context = {
        'form': form, 
    }

    return render(
        request, 
        'relatorios/relatorio.html', 
        context,
    )
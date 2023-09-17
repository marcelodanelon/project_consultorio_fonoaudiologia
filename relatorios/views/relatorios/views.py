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

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

            # [AGRUPAMENTO]
            dados_agrupados = {}
            saida_formatada = []
            # saida_formatada = ""
            for result in resultados:  
                for agrupamento in campos_agrupamento_selecionados:                  
                    valor = getattr(result, agrupamento)
                    if valor not in dados_agrupados:
                        dados_agrupados[valor] = []
                    dados_agrupados[valor].append(result)
            # consulta de campos nos dict
            # for grupo, objetos in dados_agrupados.items():
            #     saida_formatada += f'GRUPO {grupo}\n'
            #     for objeto in objetos:
            #         for campo in campos_selecionados:
            #             valor_do_campo = getattr(objeto, campo, "")  # Substitua '' pelo valor padrão desejado, se necessário
            #             saida_formatada += f'{campo}: {valor_do_campo}\n' 
            #     saida_formatada += '\n'                       
            # print(saida_formatada)

            for grupo, objetos in dados_agrupados.items():
                saida_formatada.append(f'GRUPO {grupo}')  # Adiciona o cabeçalho do grupo
                for objeto in objetos:
                    for campo in campos_selecionados:
                        valor_do_campo = getattr(objeto, campo, "")  # Substitua '' pelo valor padrão desejado, se necessário
                        saida_formatada.append(f'{campo}: {valor_do_campo}')
                saida_formatada.append('')  # Adiciona uma linha em branco após cada grupo

            # Crie uma string única unindo todas as linhas com quebras de linha HTML
            saida_html = '<br>'.join(saida_formatada)

            # [DETALHES]
            resultados = resultados.values(*campos_selecionados)

            context = {
                'form': form, 
                'campos_agrupamento_selecionados':campos_agrupamento_selecionados,
                'campos_selecionados':campos_selecionados,
                'resultados': resultados,
                'dados_agrupados': saida_html,
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
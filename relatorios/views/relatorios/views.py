from django.shortcuts import render
from django.contrib import messages
from estoque.models import ItensMovimentacaoInsumoModel, MovimentacaoInsumoModel
from django.db.models import Q
from relatorios.forms import RelatorioForm
from django.db.models import F
from datetime import datetime

def rel_movimentacao_insumos(request):
    form = RelatorioForm()

    if request.method == 'POST':
        form = RelatorioForm(request.POST)
        if form.is_valid():
            campo_agrupamento = form.cleaned_data['campos_agrupamento']
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
                if valor:
                    if campo == 'dataEntrada' or campo == 'dataValidade':
                        try:
                            valor = datetime.strptime(valor, '%d/%m/%Y').date()
                        except ValueError:
                            messages.error(request, f'A data "{valor}" não é válida no formato "dd/mm/yyyy"')
                            return render(
                                request, 
                                'relatorios/rel_movimentacao.html', 
                                {'form': form,'name_module': 'Relatórios',},
                            )
                        query &= Q(**{campo: valor})
                    if campo == 'operacao':
                        query &= Q(movimentacao__operacao=valor)
                    else:
                        query &= Q(**{campo: valor})
            for campo, valor in campos_filtro.items():
                if valor:
                    try:
                        resultados = ItensMovimentacaoInsumoModel.objects.filter(query)
                        break
                    except Exception as e:
                        error_message = str(e)
                        if "Field 'id' expected a number but got" in error_message:
                            translated_error_message = "Campo 'id' esperava um número, mas recebeu texto"
                        else:
                            translated_error_message = error_message
                        messages.error(request, translated_error_message)
                        return render(
                            request, 
                            'relatorios/rel_movimentacao.html', 
                            {'form': form, 'name_module': 'Relatórios',},
                        )

            # [INCLUINDO CAMPOS DE OUTRAS TABELAS RELACIONADAS]   
            # inclui o campo operacao da tabela de movimentacao
            if 'operacao' in campos_selecionados:
                for resultado in resultados:
                    movimentacao_id = resultado.movimentacao.id
                    operacao = MovimentacaoInsumoModel.objects.get(pk=movimentacao_id).operacao
                    resultado.operacao = operacao
            if 'operacao' in campos_selecionados:
                resultados = resultados.annotate(operacao=F('movimentacao__operacao'))

            # [AGRUPAMENTO]
            dados_agrupados = {}
            saida_formatada = []
            saida_html = []
            for result in resultados:
                if campo_agrupamento == 'operacao':
                    valor = result.movimentacao.operacao
                elif campo_agrupamento == 'dataEntrada' or campo_agrupamento == 'dataValidade':
                    valor = result.dataEntrada.strftime('%d/%m/%Y')
                else:
                    valor = getattr(result, campo_agrupamento)

                if valor not in dados_agrupados:
                    dados_agrupados[valor] = []
                dados_agrupados[valor].append(result)

            # [DETALHES AGRUPAMENTO]
            saida_formatada.append('<table border="1" style="border-collapse: collapse; width: 100%;">') 

            # Cabeçalho da tabela
            saida_formatada.append('<tr>')  
            if len(campos_selecionados) == 1:
                saida_formatada.append('<th colspan="2" style="padding: 8px; background-color: #a3a3a3;">' + campos_selecionados[0] + '</th>')  
            else:
                ## alterando cabeçalho tabela para nome verbose_name
                for campo in campos_selecionados:
                    if campo == 'local':
                        campo = 'Unidade'
                    elif campo == 'dataEntrada':
                        campo = 'Data de Entrada'
                    elif campo == 'dataValidade':
                        campo = 'Data de Validade'
                    elif campo == 'id':
                        campo = 'Id'
                    elif campo == 'movimentacao':
                        campo = 'Id Movimentação'
                    elif campo == 'insumo':
                        campo = 'Insumo'
                    elif campo == 'valorUnitario':
                        campo = 'Valor Unitário'
                    elif campo == 'valorTotal':
                        campo = 'Valor Total'
                    elif campo == 'quantidade':
                        campo = 'Quantidade'
                    elif campo == 'valorCompra':
                        campo = 'Valor Compra'
                    elif campo == 'serie':
                        campo = 'Série/Lote'
                    elif campo == 'operacao':
                        campo = 'Operação'
                    saida_formatada.append('<th style="padding: 8px; background-color: #a3a3a3;">' + campo + '</th>')  
            saida_formatada.append('</tr>') 

            for grupo, objetos in dados_agrupados.items():
                total_registros_grupo = len(objetos) 
                saida_formatada.append('<tr>')
                for campo in campos_selecionados:
                    ## alterando nome agrupamento para verbose_name de cada grupo
                    if campo == campos_selecionados[0]:
                        header_text = campo + ': ' + str(grupo)
                        if campo_agrupamento == 'local':
                            header_text = 'Unidade: ' + str(grupo)
                        elif campo_agrupamento == 'dataEntrada':
                            header_text = 'Data de Entrada: ' + grupo
                        elif campo_agrupamento == 'dataValidade':
                            header_text = 'Data de Validade: ' + grupo
                        elif campo_agrupamento == 'id':
                            header_text = 'Id: ' + str(grupo)
                        elif campo_agrupamento == 'movimentacao':
                            header_text = 'Id Movimentação: ' + str(grupo)
                        elif campo_agrupamento == 'insumo':
                            header_text = 'Insumo: ' + str(grupo)
                        elif campo_agrupamento == 'valorUnitario':
                            header_text = 'Valor Unitário: ' + grupo
                        elif campo_agrupamento == 'valorTotal':
                            header_text = 'Valor Total: ' + grupo
                        elif campo_agrupamento == 'quantidade':
                            header_text = 'Quantidade: ' + str(grupo)
                        elif campo_agrupamento == 'serie':
                            header_text = 'Série/Lote: ' + grupo
                        elif campo_agrupamento == 'operacao':
                            header_text = 'Operação: ' + grupo

                        if len(campos_selecionados) == 1:
                            saida_formatada.append('<th style="background-color: #ccc; text-align: left;">' + header_text + '</th>')
                        else:
                            saida_formatada.append('<th colspan="' + str(len(campos_selecionados) - 1) + '" style="background-color: #ccc; text-align: left;">' + header_text + '</th>')
                        saida_formatada.append('<th style="background-color: #ccc; text-align: right;">Total: ' + str(total_registros_grupo) + '</th>')
                    else:
                        saida_formatada.append('<th></th>')
                saida_formatada.append('</tr>')

                for objeto in objetos:
                    saida_formatada.append('<tr>')
                    for campo in campos_selecionados:
                        valor_do_campo = getattr(objeto, campo, "")
                        if campo == 'dataEntrada' or campo == 'dataValidade':
                            valor_do_campo = valor_do_campo.strftime('%d/%m/%Y')
                        saida_formatada.append('<td style="padding: 2px;">' + str(valor_do_campo) + '</td>')  
                    saida_formatada.append('</tr>')  

            saida_formatada.append('</table>')
            saida_html = '\n'.join(saida_formatada)

            # [DETALHES] [opcional para visualização]
            resultados = resultados.values(*campos_selecionados)

            context = {
                'form': form, 
                'campo_agrupamento':campo_agrupamento,
                'campos_selecionados':campos_selecionados,
                'campos_filtros': query,
                'resultados': resultados,
                'dados_agrupados': saida_html,
                'name_module': 'Relatórios',
            }

            return render(
                request, 
                'relatorios/rel_movimentacao.html', 
                context,
            )

    context = {
        'form': form, 
        'name_module': 'Relatórios',
    }

    return render(
        request, 
        'relatorios/rel_movimentacao.html', 
        context,
    )
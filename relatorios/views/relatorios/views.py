from django.shortcuts import render
from django.contrib import messages
from estoque.models import ItensMovimentacaoInsumoModel, MovimentacaoInsumoModel
from django.db.models import Q
from datetime import datetime
from relatorios.forms import RelatorioForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import pandas as pd
from io import BytesIO
import pandas as pd

def rel_movimentacao_insumos(request):
    form = RelatorioForm()

    context = {
        'form': form, 
        'name_module': 'Relatórios',
    }

    return render(
        request, 
        'relatorios/rel_movimentacao.html', 
        context,
    )

def render_to_pdf(template_path, context_dict):
    template = get_template(template_path)
    html_string = template.render(context_dict)

    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html_string.encode("UTF-8")), response, encoding="UTF-8")

    if not pdf.err:
        response.seek(0)
        return response

    return HttpResponse('Erro ao gerar o PDF', content_type='text/plain')

def teste(request):
    if request.method == 'POST':
        form = RelatorioForm(request.POST)
        resultados = ItensMovimentacaoInsumoModel.objects.all()
        if form.is_valid():
            campo_agrupamento = form.cleaned_data['campos_agrupamento']
            campos_selecionados = form.cleaned_data['campos']

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
                
        # Criar uma lista de dicionários com os dados dos clientes
        dados = {}
        coluna_retirar = None
        if campo_agrupamento not in campos_selecionados:
            coluna_retirar = campo_agrupamento
            campos_selecionados.insert(0, campo_agrupamento)
        for campo in campos_selecionados:
            dados[campo] = [getattr(item, campo) for item in resultados]

        df = pd.DataFrame(dados)

        # Pré-processar os dados para tornar acessíveis no template
        relatorios = []
        for nome_grupo in df[campo_agrupamento].unique():
            grupo_dados = df[df[campo_agrupamento] == nome_grupo]

            # Remover a coluna especificada por coluna_retirar do grupo de dados e do cabeçalho
            if coluna_retirar in grupo_dados.columns:
                grupo_dados = grupo_dados.drop(columns=[coluna_retirar])

            colunas = grupo_dados.columns.tolist()
            dados = grupo_dados.values.tolist()

            total_registros = len(grupo_dados)

            relatorios.append({
                'agrupamento': nome_grupo,
                'colunas': colunas,
                'dados': dados,
                'total_registros': total_registros,
            })
        
        # Renderizar o template em um PDF
        pdf = render_to_pdf('relatorios/teste.html', {'relatorios': relatorios})

        # Responda com o PDF e force o download ou abra em uma nova guia
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'
        return response

    return render(request, 'relatorios/rel_movimentacao.html', {'form': RelatorioForm(), 'name_module': 'Relatórios'})


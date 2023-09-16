from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from django.db.models import Q
from reportlab.lib.styles import getSampleStyleSheet
from django.contrib import messages
from estoque.models import ItensMovimentacaoInsumoModel
from relatorios.forms import RelatorioForm
from datetime import date
from django.contrib import messages

def sua_view_de_relatorio_pdf(request):
    form = RelatorioForm()
    dados_agrupados = {}

    if request.method == 'POST':
        form = RelatorioForm(request.POST)
        if form.is_valid():
            campos_selecionados = form.cleaned_data['campos']
            campos_agrupamento_selecionados = form.cleaned_data['campos_agrupamento']
            campo_filtro = form.cleaned_data['campo_filtro']
            filtro_valor = form.cleaned_data.get('filtro_valor', None)

            # Construa a consulta com base nas seleções do formulário
            query = Q()
            for campo in campos_selecionados:
                if campo_filtro and filtro_valor:
                    # Verifique se o campo está em campos_agrupamento_selecionados
                    if campo in campos_agrupamento_selecionados:
                        lookup = f'{campo}__{campo_filtro}'
                    else:
                        lookup = campo_filtro

                    # Verifique se o campo de filtro é um campo numérico (exemplo: 'quantidade')
                    if hasattr(ItensMovimentacaoInsumoModel, lookup):
                        # Converta o filtro_valor para inteiro antes de aplicar o filtro
                        filtro_valor_int = int(filtro_valor)
                        query |= Q(**{lookup: filtro_valor_int})

            dados = ItensMovimentacaoInsumoModel.objects.filter(query)

            for obj in dados:
                agrupamento = tuple(getattr(obj, campo) for campo in campos_agrupamento_selecionados)
                if agrupamento not in dados_agrupados:
                    dados_agrupados[agrupamento] = []
                dados_agrupados[agrupamento].append(obj)

            # Verifique se há dados antes de gerar o PDF
            if not dados_agrupados:
                messages.warning(request, "Não há informações para serem apresentadas.")
            else:
                # Crie o objeto de resposta PDF
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'

                doc = SimpleDocTemplate(response, pagesize=letter)
                elements = []

                for agrupamento, objs in dados_agrupados.items():
                    header_style = getSampleStyleSheet()["Normal"]
                    header_text = f"<b>Agrupamento:</b> {' | '.join(map(str, agrupamento))}"
                    header_paragraph = Paragraph(header_text, header_style)
                    elements.append(header_paragraph)

                    table_data = [campos_selecionados]

                    for obj in objs:
                        row_data = [getattr(obj, campo) for campo in campos_selecionados]
                        table_data.append(row_data)

                    t = Table(table_data)

                    style = TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ])

                    t.setStyle(style)
                    elements.append(t)

                doc.build(elements)
                return response

    return render(request, 'relatorios/index.html', {'form': form, 'dados_agrupados': dados_agrupados})

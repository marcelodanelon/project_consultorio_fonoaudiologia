from django.shortcuts import render
from django.http import HttpResponse
from estoque.models import ItensMovimentacaoInsumoModel
from relatorios.forms import RelatorioForm
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def index(request):
    insumos_list = []
    for f in ItensMovimentacaoInsumoModel._meta.get_fields():
        if hasattr(f, 'verbose_name'):
            insumos_list.append(f.verbose_name)

    context = {
        'insumos_list': insumos_list,
    }

    return render(
        request,
        'relatorios/index.html',
        context
    )

def sua_view_de_relatorio_pdf(request):
    form = RelatorioForm()
    dados_agrupados = {}  # Inicialize a variável fora do bloco if

    if request.method == 'POST':
        form = RelatorioForm(request.POST)
        if form.is_valid():
            campos_selecionados = form.cleaned_data['campos']
            campos_agrupamento_selecionados = form.cleaned_data['campos_agrupamento']

            # Consulta ao banco de dados com base nos campos de agrupamento selecionados
            dados_agrupamento = ItensMovimentacaoInsumoModel.objects.values_list(*campos_agrupamento_selecionados)

            # Consulta ao banco de dados com base nos campos de dados selecionados
            dados = ItensMovimentacaoInsumoModel.objects.values(*campos_selecionados)

            # Organizar os dados em um dicionário onde as chaves são os campos de agrupamento
            # e os valores são os dados associados a esses campos
            for row in dados:
                agrupamento = tuple(row[campo] for campo in campos_agrupamento_selecionados)
                if agrupamento not in dados_agrupados:
                    dados_agrupados[agrupamento] = []
                dados_agrupados[agrupamento].append(row)

            # Gerar o relatório em PDF usando ReportLab
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'

            doc = SimpleDocTemplate(response, pagesize=letter)
            elements = []

            for agrupamento, dados in dados_agrupados.items():
                # Adicionar cabeçalho do agrupamento como um objeto Paragraph
                header_style = getSampleStyleSheet()["Normal"]
                header_text = f"<b>Agrupamento:</b> {' | '.join(map(str, agrupamento))}"
                header_paragraph = Paragraph(header_text, header_style)
                elements.append(header_paragraph)
                
                # Adicionar dados do agrupamento em uma tabela
                table_data = [campos_selecionados]  # Adicione cabeçalho

                # Adicione os dados
                for row in dados:
                    row_data = [row[campo] for campo in campos_selecionados]
                    table_data.append(row_data)

                t = Table(table_data)

                # Defina o estilo da tabela
                style = TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Estilo do cabeçalho
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Cor do texto do cabeçalho
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alinhamento central
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fonte em negrito para o cabeçalho
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Espaço inferior para o cabeçalho
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Estilo para os dados
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grade da tabela
                ])

                t.setStyle(style)
                elements.append(t)

            doc.build(elements)
            return response

    return render(request, 'relatorios/index.html', {'form': form, 'dados_agrupados': dados_agrupados})


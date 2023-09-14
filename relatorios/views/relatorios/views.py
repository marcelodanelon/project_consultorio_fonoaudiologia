from django.shortcuts import render
from django.http import HttpResponse
from estoque.models import ItensMovimentacaoInsumoModel
from reportlab.pdfgen import canvas

def index(request):
    insumos_list = []
    for f in ItensMovimentacaoInsumoModel._meta.get_fields():
        if hasattr(f, 'verbose_name'):
            insumos_list.append(f.verbose_name)

    context = {
        'insumos_list' : insumos_list,
    }

    return render(
        request,
        'relatorios/index.html',
        context
    )

def sua_view_de_relatorio_pdf(request):
    if request.method == 'POST':
        insumos_selecionados = request.POST.getlist('insumos_direita[]')
        data = request.POST.get('data')

        insumos = ItensMovimentacaoInsumoModel.objects.filter(dataEntrada=data)
        
        resultados = []
        for insumo in insumos:
            insumo_dict = {
                'insumo': insumo.insumo,  # Substitua 'campo1' pelos nomes reais dos campos
                'dataEntrada': insumo.dataEntrada,
                'quantidade': insumo.quantidade,
                # Adicione outros campos conforme necessário
            }
            resultados.append(insumo_dict)

        # Suponha que 'resultados' contenha os resultados da consulta agrupada
        # resultados = [
        #     {'campo_grupo': 'Grupo A', 'total': 10},
        #     {'campo_grupo': 'Grupo B', 'total': 15},
        #     {'campo_grupo': 'Grupo C', 'total': 8},
        # ]

        # Crie uma resposta HTTP com o tipo de conteúdo PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="relatorio.pdf"'

        # Crie o PDF usando o ReportLab
        p = canvas.Canvas(response)

        # Adicione título e cabeçalho
        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, 750, "Relatório Agrupado")
        p.setFont("Helvetica", 12)
        p.drawString(100, 730, "Agrupamento | Total")

        # Adicione os dados agrupados
        p.setFont("Helvetica", 12)
        y = 710
        for resultado in resultados:
            insumo = resultado['insumo']
            dataEntrada = resultado['dataEntrada']
            quantidade = resultado['quantidade']
            p.drawString(100, y, f"{insumo} | {dataEntrada} | {quantidade}")
            y -= 20

        # Fecha o PDF
        p.showPage()
        p.save()

        return response
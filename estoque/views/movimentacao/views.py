from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from estoque.models import MovimentacaoInsumoModel
from django.db.models import Q
from datetime import date, datetime

def isDate(var):
    try:
        d = datetime.strptime(var, '%d/%m/%Y').date()
        return True
    except:
        return False

@login_required(login_url='home:loginUser')
def listMovimentacaoInsumo(request):
    insumos = MovimentacaoInsumoModel.objects.all().order_by('-id')

    paginator = Paginator(insumos, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'page_obj': page_obj,
            'title':'Cadastro',
            'name_screen': 'Cadastro',
            'name_module': 'Estoque',
    }

    return render(
        request,
        'estoque/movimentacao/search.html',
        context
    )

@login_required(login_url='home:loginUser')
def searchMovimentacaoInsumo(request):
    search_movimentacao = request.GET.get('q','').strip()

    if search_movimentacao == "":
        return redirect('estoque:listMovimentacaoInsumo')

    if search_movimentacao.isnumeric():
        movimentacoes = MovimentacaoInsumoModel.objects.filter(id=int(search_movimentacao)).order_by('id')
    elif isDate(search_movimentacao):
        movimentacoes = MovimentacaoInsumoModel.objects.filter(data=datetime.strptime(search_movimentacao, '%d/%m/%Y').date()).order_by('id')
    else:        
        movimentacoes = MovimentacaoInsumoModel.objects.filter(
            Q(local__name__icontains=search_movimentacao) | 
            Q(operacao__icontains=search_movimentacao) 
        ).order_by('id')

    paginator = Paginator(movimentacoes, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Home',
            'page_obj': page_obj,
    }

    return render(
        request,
        'estoque/movimentacao/search.html',
        context
    )
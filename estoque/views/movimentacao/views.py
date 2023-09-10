from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from estoque.models import MovimentacaoInsumoModel

# Create your views here.
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
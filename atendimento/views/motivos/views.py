from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from atendimento.models import MotivosAtendimentoModel
from django.core.paginator import Paginator

@login_required(login_url='home:loginUser')
def listMotivo(request):
    form_action = reverse('atendimento:createMotivo')

    motivos = MotivosAtendimentoModel.objects.all().order_by('id')

    paginator = Paginator(motivos, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'page_obj': page_obj,
            'title':'Cadastro',
            'name_module': 'Atendimento',
            'form_action': form_action,
    }

    return render(
        request,
        'motivos/search.html',
        context
    )

@login_required(login_url='home:loginUser')
def searchMotivo(request):
    search_motivo = request.GET.get('q','').strip()

    if search_motivo == "":
        return redirect('atendimento:listMotivo')

    if search_motivo.isdigit():
        motivos = MotivosAtendimentoModel.objects.filter(id=int(search_motivo)).order_by('id')
    else:
        motivos = MotivosAtendimentoModel.objects.filter(name__icontains=search_motivo).order_by('id')

    paginator = Paginator(motivos, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Atendimento',
            'page_obj': page_obj,
    }

    return render(
        request,
        'motivos/search.html',
        context
    )
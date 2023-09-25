from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from atendimento.models import AudiometriaModel
from django.core.paginator import Paginator

@login_required(login_url='home:loginUser')
def listAudiometria(request):
    form_action = reverse('atendimento:audiometria')

    audiometrias = AudiometriaModel.objects.all().order_by('id')

    paginator = Paginator(audiometrias, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'page_obj': page_obj,
            'title':'Cadastro',
            'name_module': 'Estoque',
            'form_action': form_action,
    }

    return render(
        request,
        'audiometria/search.html',
        context
    )

@login_required(login_url='home:loginUser')
def searchAudiometria(request):
    search_audiometria = request.GET.get('q','').strip()

    if search_audiometria == "":
        return redirect('estoque:listAudiometria')

    if search_audiometria.isdigit():
        audiometrias = AudiometriaModel.objects.filter(id=int(search_audiometria)).order_by('id')

    paginator = Paginator(audiometrias, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Atendimento',
            'page_obj': page_obj,
    }

    return render(
        request,
        'audiometria/search.html',
        context
    )
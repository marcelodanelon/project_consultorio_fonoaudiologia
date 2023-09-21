from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import Group
from estoque.forms import GrupoInsumoForm
from estoque.models import GrupoInsumoModel
import ast

@login_required(login_url='home:loginUser')
def createGrupo(request):
    form_action = reverse('estoque:createGrupo')
    grupos_disponiveis = Group.objects.all()
    grupos_selecionados = []

    if request.method == 'POST':
        formGrupo = GrupoInsumoForm(request.POST)
        grupos_selecionados = request.POST.getlist('grupos_selecionados')
        if formGrupo.is_valid():
            form = formGrupo.save(commit=False)
            form.perfis = grupos_selecionados
            formGrupo.save()
            messages.success(request, 'Grupo cadastrado com sucesso!')
            return redirect('estoque:listGrupo')

        context = {
            'form': formGrupo,
            'title':'Cadastro',
            'name_module': 'Estoque',
            'grupos_disponiveis': grupos_disponiveis,
            'grupos_selecionados': grupos_selecionados,
            'form_action': form_action,
        }

        return render(
            request,
            'estoque/grupo/grupo.html',
            context
        )

    context = {
            'form': GrupoInsumoForm(),
            'title':'Cadastro',
            'name_screen': 'Cadastro',
            'name_module': 'Estoque',
            'grupos_disponiveis': grupos_disponiveis,
            'grupos_selecionados': grupos_selecionados,
            'form_action': form_action,
    }

    return render(
        request,
        'estoque/grupo/grupo.html',
        context
    )

@login_required(login_url='home:loginUser')
def updateGrupo(request, grupo_id):
    grupo = get_object_or_404(GrupoInsumoModel, pk=grupo_id)
    form_action = reverse('estoque:updateGrupo', args=(grupo_id,))
    grupos_selecionados = []
    if request.method == 'POST':
        grupos_selecionados = request.POST.getlist('grupos_selecionados[]')
        formGrupo = GrupoInsumoForm(request.POST, instance=grupo)
        if formGrupo.is_valid():
            form = formGrupo.save(commit=False)
            form.perfis = grupos_selecionados
            formGrupo.save()
            messages.success(request, 'Grupo atualizado com sucesso!')
            return redirect('estoque:listGrupo')

        context = {
            'form' : GrupoInsumoForm(instance=grupo),
            'form_action': form_action,
            'title':'Cadastro',
            'grupos_disponiveis': grupos_disponiveis,
            'grupos_selecionados': grupos_selecionados,
            'name_module': 'Estoque',
            'option_delete': 'yes',
        }

        return render(
            request,
            'estoque/grupo/grupo.html',
            context
        )
    
    perfis_str = grupo.perfis
    try:
        nomes_grupos = ast.literal_eval(perfis_str)
    except (SyntaxError, ValueError):
        nomes_grupos = [perfis_str]

    if nomes_grupos:
        grupos_selecionados = []  
        grupos_disponiveis = []  
        
        for nome_grupo in nomes_grupos:
            grupo_atual = Group.objects.filter(name=nome_grupo).first()
            if grupo_atual:
                grupos_selecionados.append(grupo_atual)
        
        grupos_disponiveis = list(Group.objects.all().exclude(id__in=[grupo.id for grupo in grupos_selecionados]))
    else:
        grupos_disponiveis = list(Group.objects.all())
        grupos_selecionados = []

    context = {
        'form' : GrupoInsumoForm(instance=grupo),
        'form_action': form_action,
        'title':'Cadastro',
        'grupos_disponiveis': grupos_disponiveis,
        'grupos_selecionados': grupos_selecionados,
        'name_module': 'Estoque',
        'option_delete': 'yes',
    }

    return render(
        request,
        'estoque/grupo/grupo.html',
        context
    )
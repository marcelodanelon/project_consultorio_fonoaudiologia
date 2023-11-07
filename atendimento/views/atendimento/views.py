from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.contrib import messages
from datetime import date
from django.db.models import F, Case, When, Value, CharField
from atendimento.forms import AtendimentoForm, AnamneseForm, ContatosTelefonicosForm
from atendimento.models import AtendimentoModel, AnamneseModel, ContatosTelefonicosModel, AudiometriaModel
from home.models import ClientModel, ProfessionalModel, LocalModel
from estoque.models import MovimentacaoInsumoModel, ItensMovimentacaoInsumoModel
from agendamento.models import AgendamentoModel

@login_required(login_url='home:loginUser')
def getJSONclient(request):
    if request.GET.get('searchClient'):
        q = request.GET.get('searchClient')
        model = list(ClientModel.objects.filter(first_name__contains=q).values('id', 'first_name','last_name', 'born', 'document1'))
        return JsonResponse(data={'results': model})

@login_required(login_url='home:loginUser')
def index(request):
    # Criação primeiro gráfico por Atendimento
    count = int(ProfessionalModel.objects.all().count())
    professionals = list(ProfessionalModel.objects.all())
    data_points1 = []
    for i in range(count):
        professional = AtendimentoModel.objects.filter(aProfessional=professionals[i])
        if not professional != None:
            data_points1.append({'label': 'Sem registros', "y": 0})
            break
        else:
            data_points1.append({'label': str(professional.first().aProfessional), "y": professional.count()})

    # Criação segundo gráfico por Unidade
    count = int(LocalModel.objects.all().count())
    locais = list(LocalModel.objects.all())
    data_points2 = []
    for i in range(count):
        local = AtendimentoModel.objects.filter(aLocal=locais[i])
        if not local != None:
            data_points2.append({'label': 'Sem registros', "y": 0})
            break
        else:
            data_points2.append({'label': locais[i].name, "y": local.count()})

    # Criação terceiro gráfico por mês no ano atual (Anamnese)
    data_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    data_points3 = []
    for i in range(12):
        meses = AnamneseModel.objects.filter(aDataAna__month=i).filter(aDataAna__year=date.today().year)
        if meses.count() != 0:
            data_points3.append({'label': data_meses[i], "y": meses.count()})

    # Criação quarto gráfico por mês no ano atual (1º Atendimento)
    data_points4 = []
    for i in range(12):
        meses = AtendimentoModel.objects.filter(aDataPri__month=i).filter(aDataPri__year=date.today().year)
        if meses.count() != 0:
            data_points4.append({'label': data_meses[i], "y": meses.count()})

    context = {
        'title': 'Home',
        'name_module': 'Home',
        'data_points' : data_points1,
        'data_points2' : data_points2,
        'data_points3' : data_points3,
        'data_points4' : data_points4,
        'name_module': 'Atendimento',
        'title': 'Atendimento',
    }

    return render(
        request,
        'atendimento/index.html',
        context
    )

@login_required(login_url='home:loginUser')
def atendimento(request):
    form_action = reverse('atendimento:atendimento')
    order_forms = AtendimentoModel()
    anam_order_formset = inlineformset_factory(AtendimentoModel, AnamneseModel, form=AnamneseForm, extra=0, can_delete=True, min_num=1)
    tele_order_formset = inlineformset_factory(AtendimentoModel, ContatosTelefonicosModel, form=ContatosTelefonicosForm, extra=0, can_delete=True, min_num=1)
    if request.method == 'POST':
        try:
            search = int(request.POST.get('clientId'))
            client = ClientModel.objects.filter(pk=search)
        except:
            search = None
            client = None

        agendamento_id = request.POST.get('agendamentoId')
        if agendamento_id:
            agendamento_id = int(agendamento_id)
            agendamento = get_object_or_404(AgendamentoModel, id=agendamento_id)
            agendamento.agSituac = 'atendido'
            agendamento.save()

        updateAtend = int(request.POST.get('updateAtendimento'))
        forms = AtendimentoForm(request.POST, request.FILES, instance=order_forms)
        formAnamSet = anam_order_formset(request.POST, request.FILES, instance=order_forms)
        formTeleSet = tele_order_formset(request.POST, request.FILES, instance=order_forms)

        if updateAtend == 1:
            atendimento = AtendimentoModel.objects.filter(aClient=search).filter(aSituaca='Em Andamento').get()
            forms = AtendimentoForm(request.POST, instance=atendimento)

            formAnamSet = anam_order_formset(request.POST, instance=atendimento)
            formTeleSet = tele_order_formset(request.POST, instance=atendimento)

            has_errors = any(error_dict for error_dict in formTeleSet.errors)
            if has_errors:
                messages.error(request, formTeleSet.errors)
            has_errors = any(error_dict for error_dict in formAnamSet.errors)
            if has_errors:
                messages.error(request, formAnamSet.errors)
            has_errors = any(error_dict for error_dict in forms.errors)
            if has_errors:
                messages.error(request, forms.errors)

            if forms.is_valid() and formAnamSet.is_valid() and formTeleSet.is_valid():
                for delete_value in formAnamSet.deleted_forms:
                    if delete_value.instance.pk:
                        delete_value.instance.delete()
                for delete_value in formTeleSet.deleted_forms:
                    if delete_value.instance.pk:
                        delete_value.instance.delete()

                form_t = forms.save(commit=False)     
                form_t_tel = formTeleSet.save(commit=False) 
                for i in form_t_tel:
                    i.aDemanda = form_t.aDemanda 
                formAnamSet.save()  
                formTeleSet.save()
                forms.save()
                messages.success(request, 'Atendimento atualizado com sucesso!')
                return redirect('atendimento:index') 
            
        if forms.is_valid() and formAnamSet.is_valid() and formTeleSet.is_valid():
            form_t = forms.save(commit=False)     
            form_t_tel = formTeleSet.save(commit=False) 
            for i in form_t_tel:
                i.aDemanda = form_t.aDemanda
            formAnamSet.save() 
            formTeleSet.save()
            forms.save()
            messages.success(request, 'Atendimento gravado com sucesso!')
            return redirect('atendimento:index')
    else:
        forms = AtendimentoForm(instance=order_forms)
        formAnamSet = anam_order_formset(instance=order_forms)
        formTeleSet = tele_order_formset(instance=order_forms)

        #inicio de um novo atendimento | BUSCA MÉTODO GET
        try:
            search = int(request.GET.get('searchClient'))
            client = ClientModel.objects.filter(pk=search)
        except:
            search = None
            client = None

        #verifica se há atendimento em andamento
        try:
            atendimento = AtendimentoModel.objects.filter(aClient=search).filter(aSituaca='Em Andamento').get()
            if atendimento.aSituaca != 'Concluído':
                updateAtend = 1
                forms = AtendimentoForm(instance=atendimento)
                anams = AnamneseModel.objects.filter(aIDAtend=atendimento)
                teles = ContatosTelefonicosModel.objects.filter(aIDAtend=atendimento).order_by('-id')
                formAnamSet = anam_order_formset(instance=atendimento, queryset=anams)
                formTeleSet = tele_order_formset(instance=atendimento, queryset=teles)
            else:
                updateAtend = 0
        except AtendimentoModel.DoesNotExist:
            updateAtend = 0

    context = {
        'form': forms,
        'formAnamSet': formAnamSet,
        'formTeleSet': formTeleSet,
        'name_module': 'Atendimento',
        'form_action': form_action,
        'title': 'Atendimento',
        'client': client,
        'updateAtend': updateAtend,
    }

    return render(request, 'atendimento/atendimento.html', context)

@login_required(login_url='home:loginUser')
def historicoAtendimento(request):
    form_atendimento = AtendimentoForm()

    try:
        search = int(request.GET.get('searchClient'))
        client = ClientModel.objects.filter(pk=search).get()               
    except:
        search = None
        client = None

    client_atendimentos = AtendimentoModel.objects.filter(aClient=client)
    client_anamneses = AnamneseModel.objects.none()
    for i in range(client_atendimentos.count()):
        client_anamneses = client_anamneses.union(AnamneseModel.objects.filter(aIDAtend=client_atendimentos[i]))
    client_telefonemas = ContatosTelefonicosModel.objects.filter(aIDAtend__aClient=client)

    from django.db.models import F

    client_saida = MovimentacaoInsumoModel.objects.exclude(eClient=None).filter(eClient=client)


    client_saida_com_nome_insumo = []

    for movimentacao in client_saida:
        itens_insumo = ItensMovimentacaoInsumoModel.objects.filter(movimentacao=movimentacao)
        
        for item in itens_insumo:
            descricao_insumo = item.insumo.descricao
            client_saida_com_nome_insumo.append({
                'movimentacao_id': movimentacao.id,
                'nome_insumo': descricao_insumo
            })
    for client_saida_item in client_saida_com_nome_insumo:
        print(f'Movimentação ID: {client_saida_item["movimentacao_id"]}, Nome do Insumo: {client_saida_item["nome_insumo"]}')

    client_saida = MovimentacaoInsumoModel.objects.exclude(eClient=None).filter(eClient=client)

    client_saida = client_saida.annotate(
        nome_insumo=Case(
            When(itensmovimentacaoinsumomodel__movimentacao=F('id'), then=F('itensmovimentacaoinsumomodel__insumo__descricao')),
            default=Value(''), output_field=CharField()
        )
    )

    client_audiometria = AudiometriaModel.objects.filter(aClient=client)

    client_agendamentos = AgendamentoModel.objects.filter(aClient=client)
    for i in client_agendamentos:
        i.agDataAg = i.agDataAg.strftime("%d/%m/%Y")

    context = {
        'form_atendimento': form_atendimento,
        'atendimentos': client_atendimentos,
        'telefonemas': client_telefonemas,
        'anamneses': client_anamneses,
        'saidasEstoque': client_saida,
        'audiometrias': client_audiometria,
        'agendamentos': client_agendamentos,
        'name_module': 'Atendimento',
        'title': 'Atendimento',
    }

    return render(
        request,
        'atendimento/historicoAtendimento.html',
        context
    )

def atendimento_new(request):
    atendimentoForm = AtendimentoForm()
    telefonemasFormset = inlineformset_factory(AtendimentoModel, ContatosTelefonicosModel, form=ContatosTelefonicosForm, extra=0, can_delete=True, min_num=1)
    telefonemasForm = telefonemasFormset(instance=AtendimentoModel())
    regulagensFormset = inlineformset_factory(AtendimentoModel, AnamneseModel, form=AnamneseForm, extra=0, can_delete=True, min_num=1)
    regulagemForm = regulagensFormset(instance=AtendimentoModel())

    context={
        'atendimentoForm': atendimentoForm,
        'telefonemasForm': telefonemasForm,
        'regulagemForm': regulagemForm,
    }

    return render(
        request,
        'atendimento_new/atendimento.html',
        context
    )
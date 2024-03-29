from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from agendamento.models import AgendaModel, AgendamentoModel
from django.http import JsonResponse
from datetime import datetime, date
from django.db.models import Count
from django.db.models import Q

def isDate(var):
    try:
        d = datetime.strptime(var, '%d/%m/%Y').date()
        return True
    except:
        return False

@login_required(login_url='home:loginUser')
def getJSONdatas(request):
    if request.GET.get('local') and request.GET.get('profissional'):
        local = int(request.GET.get('local'))
        profissional = int(request.GET.get('profissional'))
        motivo = int(request.GET.get('motivo'))
        model = AgendaModel.objects.filter(aLocal=local).filter(aProfessional=profissional).filter(aMotAten=motivo).filter(agDatFim__gte=date.today()).values()
        agendamentos_com_vagas = [] 

        for i in model:
            agenda_id = i['id']
            if i['agTipAge'] == 'quantidade':                
                agendadosQtdTotal = AgendamentoModel.objects.filter(agAgenda=agenda_id).values('agDataAg').annotate(total=Count('agDataAg'))
                for item in agendadosQtdTotal:
                    data_agenda = item['agDataAg']
                    total_registros = item['total']                
                    vagas = i['agQtdTot']
                    vagas_restantes = vagas - total_registros 
                    i['vagasRestantes'] = vagas_restantes 

                    info_dict = {
                        'Agenda': agenda_id,
                        'Data': data_agenda,
                        'Total': vagas,
                        'Utilizado': total_registros,
                        'Restantes': vagas_restantes
                    }
                    agendamentos_com_vagas.append(info_dict)
                model = list(model)
                return JsonResponse(data={'results': model,'agendamentos': agendamentos_com_vagas})
            else:
                agendadosQtdTempo = AgendamentoModel.objects.filter(agAgenda=agenda_id).values('agDataAg','agHoraAg')
                for item in agendadosQtdTempo:
                    data_agenda = item['agDataAg']
                    hora_agenda = item['agHoraAg']

                    info_dict = {
                        'Agenda': agenda_id,
                        'Data': data_agenda,
                        'Hora': hora_agenda
                    }
                    agendamentos_com_vagas.append(info_dict)
                print(agendamentos_com_vagas)
                model = list(model)
                return JsonResponse(data={'results': model,'agendamentos': agendamentos_com_vagas})            
        
@login_required(login_url='home:loginUser')
def getJSONhorarios(request):
    if request.GET.get('local') and request.GET.get('profissional') and request.GET.get('data'):
        local = int(request.GET.get('local'))
        profissional = int(request.GET.get('profissional'))
        data_str = request.GET.get('data')
        data = datetime.strptime(data_str, '%d/%m/%Y').date()  
        agenda = int(request.GET.get('agenda'))

        agendas = AgendaModel.objects.filter(aLocal=local).filter(aProfessional=profissional)
        dados_horarios = []
        for agenda in agendas:
            if  data >= agenda.agDatIni and data <= agenda.agDatFim:
                if agenda.agTipAge == 'quantidade':
                    quantidade = agenda.agQtdTot
                    tipoAgenda = agenda.agTipAge
                    dados_horarios.append({'agenda':agenda.pk,'quantidade': quantidade, 'tipoAgenda': tipoAgenda})
                    break
                else:
                    quantidade = agenda.agQtdTot
                    tempo = agenda.agQtdTem
                    tipoAgenda = agenda.agTipAge
                    dados_horarios.append({'agenda':agenda.pk,'quantidade': quantidade, 'tipoAgenda': tipoAgenda, 'tempo': tempo})
                    break                   

        return JsonResponse(data={'results': dados_horarios})

@login_required(login_url='home:loginUser')
def listAgendamento(request):
    form_action = reverse('agendamento:createAgendamento')

    agendamentos = AgendamentoModel.objects.all().order_by('id')

    paginator = Paginator(agendamentos, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'page_obj': page_obj,
            'title':'Cadastro',
            'name_module': 'Agendamento',
            'form_action': form_action,
    }

    return render(
        request,
        'agendamento/agendamento/search.html',
        context
    )

@login_required(login_url='home:loginUser')
def searchAgendamento(request):
    search_agendamento = request.GET.get('q','').strip()

    if search_agendamento == "":
        return redirect('agendamento:listAgendamento')

    if search_agendamento.isnumeric():
        agendamentos = AgendamentoModel.objects.filter(id=int(search_agendamento)).order_by('id')
    elif isDate(search_agendamento):
        agendamentos = AgendamentoModel.objects.filter(agDataAg=datetime.strptime(search_agendamento, '%d/%m/%Y').date()).order_by('id')
    else:        
        agendamentos = AgendamentoModel.objects.filter(
            Q(aProfessional__first_name__icontains=search_agendamento) |
            Q(aProfessional__last_name__icontains=search_agendamento) | 
            Q(aClient__first_name__icontains=search_agendamento) |
            Q(aClient__last_name__icontains=search_agendamento) | 
            Q(aLocal__name__icontains=search_agendamento) 
        ).order_by('id')

    paginator = Paginator(agendamentos, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Agendamento',
            'page_obj': page_obj,
    }

    return render(
        request,
        'agendamento/agendamento/search.html',
        context
    )
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from agendamento.models import AgendaModel, AgendamentoModel
from django.http import JsonResponse
from datetime import datetime, date
from django.db.models import Count

@login_required(login_url='home:loginUser')
def getJSONdatas(request):
    if request.GET.get('local') and request.GET.get('profissional'):
        local = int(request.GET.get('local'))
        profissional = int(request.GET.get('profissional'))
        model = AgendaModel.objects.filter(aLocal=local).filter(aProfessional=profissional).filter(agDatFim__gte=date.today()).values()
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
                    # agendadosQtdTotal = AgendamentoModel.objects.filter(agAgenda=agenda).filter(agDataAg=data)
                    # agendadosQtdTotal = agendadosQtdTotal.count()
                    # quantidade = quantidade - agendadosQtdTotal
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
def index(request):

    context = {
        'name_module': 'Agendamento',
    }

    return render(
        request,
        "agendamento/index.html",
        context
    )

@login_required(login_url='home:loginUser')
def listAgenda(request):
    form_action = reverse('agendamento:createAgenda')

    agendas = AgendaModel.objects.all().order_by('id')

    paginator = Paginator(agendas, 14)
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
        'agendamento/agenda/search.html',
        context
    )

@login_required(login_url='home:loginUser')
def searchAgenda(request):
    search_agenda = request.GET.get('q','').strip()

    if search_agenda == "":
        return redirect('agendamento:listAgenda')

    if search_agenda.isdigit():
        agendas = search_agenda.objects.filter(id=int(search_agenda)).order_by('id')

    paginator = Paginator(agendas, 14)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
            'title':'Pesquisa',
            'name_module': 'Agendamento',
            'page_obj': page_obj,
    }

    return render(
        request,
        'agendamento/agenda/search.html',
        context
    )
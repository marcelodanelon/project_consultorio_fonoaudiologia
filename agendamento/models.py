from django.db import models
from home.models import ProfessionalModel, LocalModel, ClientModel
from atendimento.models import MotivosAtendimentoModel

# Create your models here.
class AgendaModel(models.Model):
    aProfessional = models.ForeignKey(ProfessionalModel, on_delete=models.PROTECT, verbose_name='Profissional')
    aLocal = models.ForeignKey(LocalModel, on_delete=models.PROTECT, verbose_name='Unidade')
    agDatIni = models.DateField(verbose_name='Data Início')
    agDatFim = models.DateField(verbose_name='Data Final')
    agHorIni = models.TimeField(verbose_name='Horário Início')
    agHorFim = models.TimeField(verbose_name='Horário Final')
    agTipAge = models.CharField(max_length=30 ,verbose_name='Tipo de Agenda', choices=(['quantidade','Quantidade'],['quantidadeTempo','Quantidade por tempo']), default='quantidade')
    aMotAten = models.ForeignKey(MotivosAtendimentoModel, on_delete=models.PROTECT, verbose_name="Motivo de Agendamento", null=True)
    agQtdTot = models.IntegerField(verbose_name='Quantidade', blank=True, null=True)
    agQtdTem = models.IntegerField(verbose_name='Tempo', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.id} - Profissional: {self.aProfessional}'
    
class AgendamentoModel(models.Model):
    aClient = models.ForeignKey(ClientModel, on_delete=models.PROTECT, verbose_name='Cliente')
    aProfessional = models.ForeignKey(ProfessionalModel, on_delete=models.PROTECT, verbose_name='Profissional')
    aLocal = models.ForeignKey(LocalModel, on_delete=models.PROTECT, verbose_name='Unidade')
    aMotAten = models.ForeignKey(MotivosAtendimentoModel, on_delete=models.PROTECT, verbose_name="Motivo de Atendimento", null=True)
    agDataAg = models.DateField(verbose_name='Data Agendamento')
    agHoraAg = models.TimeField(verbose_name='Horário Agendamento')
    agObserv = models.TextField(verbose_name='Observações', blank=True, null=True)
    agSituac = models.CharField(max_length=30, verbose_name='Situação', choices=(['agendado','Agendado'],['atendido','Atendido']), default='agendado', blank=True)
    agAgenda = models.ForeignKey(AgendaModel, on_delete=models.PROTECT, verbose_name='Agenda', default=1)

    def __str__(self) -> str:
        return f'{self.id} Cliente: {self.aClient} Data: {self.agDataAg} - {self.agHoraAg}'
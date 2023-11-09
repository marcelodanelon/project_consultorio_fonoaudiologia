from django.db import models
from home.models import ClientModel, ProfessionalModel, LocalModel
from datetime import date

CHOICES_OUVIDO = [
    ("OE" ,"Ouvido Esquerdo"),
    ("OD" ,"Ouvido Direito"),
    ("Ambos" ,"Ambos"),
]

class MotivosAtendimentoModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Descrição")

    def __str__(self) -> str:
        return f'{self.name}'

class AtendimentoModel(models.Model):
    aClient = models.ForeignKey(ClientModel, verbose_name="Cliente", on_delete=models.SET_NULL, null=True)
    aProfessional = models.ForeignKey(ProfessionalModel, verbose_name="Profissional", on_delete=models.SET_NULL, null=True)
    aLocal = models.ForeignKey(LocalModel, verbose_name="Unidade de Atendimento", on_delete=models.SET_NULL, null=True)
    aDataAte = models.DateField(default=date.today, verbose_name="Data")
    aMotAten = models.ForeignKey(MotivosAtendimentoModel, on_delete=models.PROTECT, verbose_name="Motivo de Atendimento", null=True)
    aDataPri = models.DateField(verbose_name="Data 1ª consulta", null=True, blank=True)
    aDemanda = models.CharField(max_length=15, choices=[('espontanea', 'Espontânea'), ('telefone', 'Telefone'), ('agendamento', 'Agendamento')], default='espontanea', verbose_name='Demanda')
    aObsAten = models.TextField(blank=True, null=True, verbose_name='Observações')
    aConhece = models.CharField(max_length=50, null=True, blank=True)
    aDifiEsc = models.CharField(max_length=50, null=True, blank=True)
    aDifiPio = models.CharField(max_length=50, null=True, blank=True)
    aOuviMel = models.CharField(max_length=50, null=True, blank=True)
    aPessFam = models.CharField(max_length=50, null=True, blank=True)
    aTrabRui = models.CharField(max_length=50, null=True, blank=True)
    aTelevis = models.BooleanField(blank=True, default=False)
    aTeleFix = models.BooleanField(blank=True, default=False)
    aTeleCel = models.BooleanField(blank=True, default=False)
    aConvGru = models.BooleanField(blank=True, default=False)
    aConvRui = models.BooleanField(blank=True, default=False)
    aFalaBai = models.BooleanField(blank=True, default=False)
    aFaladis = models.BooleanField(blank=True, default=False)
    aCineTea = models.BooleanField(blank=True, default=False)
    aPaleSal = models.BooleanField(blank=True, default=False)
    aOutrDif = models.CharField(max_length=50, null=True, blank=True)
    aZumbido = models.BooleanField(blank=True, default=False)
    aCoceira = models.BooleanField(blank=True, default=False)
    aOtiteOO = models.BooleanField(blank=True, default=False)
    aDorOOOO = models.BooleanField(blank=True, default=False)
    aCiruOuv = models.BooleanField(blank=True, default=False)
    aTimpPer = models.BooleanField(blank=True, default=False)
    aSensTam = models.BooleanField(blank=True, default=False)
    aOutrOuv = models.CharField(max_length=50, null=True, blank=True)
    aCardiop = models.BooleanField(blank=True, default=False)
    aPresAlt = models.BooleanField(blank=True, default=False)
    aProbRin = models.BooleanField(blank=True, default=False)
    aTontura = models.BooleanField(blank=True, default=False)
    aDiabete = models.BooleanField(blank=True, default=False)
    aProbTir = models.BooleanField(blank=True, default=False)
    aUsoOtot = models.BooleanField(blank=True, default=False)
    aColeAlt = models.BooleanField(blank=True, default=False)
    aLabirin = models.BooleanField(blank=True, default=False)
    aCancerO = models.BooleanField(blank=True, default=False)
    aOutrDoe = models.CharField(max_length=50, null=True, blank=True)
    aJaUsoAp = models.CharField(max_length=5, choices=[('sim', 'Sim'), ('não', 'Não')], null=True, blank=True)
    aMarcaOO = models.CharField(max_length=50, null=True, blank=True)
    aTempoOO = models.CharField(max_length=50, null=True, blank=True)
    aJaTesAp = models.CharField(max_length=5, choices=[('sim', 'Sim'), ('não', 'Não')], null=True, blank=True)
    aQualApa = models.CharField(max_length=50, null=True, blank=True)
    aApaIndi = models.CharField(max_length=50, null=True, blank=True)
    aValApar = models.CharField(max_length=50, null=True, blank=True)
    aLadoInd = models.CharField(max_length=50, choices=CHOICES_OUVIDO, null=True, blank=True)
    aFormPag = models.CharField(max_length=50, null=True, blank=True)
    aSaiTest = models.DateField(blank=True, null=True)
    aRetTest = models.DateField(blank=True, null=True)
    aComClik = models.CharField(max_length=5, choices=[('sim', 'Sim'), ('não', 'Não')], null=True, blank=True)
    aSemClik = models.CharField(max_length=5, choices=[('sim', 'Sim'), ('não', 'Não')], null=True, blank=True)
    aClikOOD = models.CharField(max_length=50, null=True, blank=True)
    aClikOOE = models.CharField(max_length=50, null=True, blank=True)
    aTuboOOD = models.CharField(max_length=50, null=True, blank=True)
    aTuboOOE = models.CharField(max_length=50, null=True, blank=True)
    aReceOOD = models.CharField(max_length=50, null=True, blank=True)
    aReceOOE = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.pk} - {self.aDataAte} {self.aClient}'
    
class ContatosTelefonicosModel(models.Model):
    aIDAtend = models.ForeignKey(AtendimentoModel, on_delete=models.PROTECT, null=True, blank=True)
    aTelLiga = models.CharField(max_length=20, verbose_name='Telefone',blank=True, null=True,)
    aTelObse = models.CharField(max_length=50,blank=True, null=True, verbose_name='Observações')

    def __str__(self):
        return f'{self.aTelLiga}'

class RegulagemModel(models.Model):
    aIDAtend = models.ForeignKey(AtendimentoModel, on_delete=models.CASCADE, null=True, blank=True)
    aAjustOD = models.CharField(max_length=50, null=True, blank=True)
    aAjustOE = models.CharField(max_length=50, null=True, blank=True)
    aAObserv = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return f'ID: {self.pk} - IDAtend: {self.aIDAtend}'
    
class AudiometriaModel(models.Model):
    aClient = models.ForeignKey(ClientModel, verbose_name="Cliente", on_delete=models.PROTECT, null=True)
    auData = models.DateField(default=date.today, verbose_name='Data')
    auProfessional = models.ForeignKey(ProfessionalModel, verbose_name="Profissional", on_delete=models.SET_NULL, null=True)
    auLocal = models.ForeignKey(LocalModel, verbose_name="Unidade", on_delete=models.SET_NULL, null=True)
    auAudio = models.CharField(max_length=50, blank=True, null=True, verbose_name='Audiômetro')
    auCalib = models.DateField(blank=True, null=True, verbose_name='Calibração')
    auMedSo = models.CharField(max_length=50, blank=True, null=True, verbose_name='Médico Solicitante')
    auMVaOe = models.CharField(max_length=30, blank=True, null=True, verbose_name='MASC. VA (OE)')
    auMVoOe = models.CharField(max_length=30, blank=True, null=True, verbose_name='MASC. VO (OE)')
    auMVaOd = models.CharField(max_length=30, blank=True, null=True, verbose_name='MASC. VA (OD)')
    auMVoOd = models.CharField(max_length=30, blank=True, null=True, verbose_name='MASC. VO (OD)')
    auMosPoOe = models.CharField(max_length=3, blank=True, null=True, verbose_name='%')
    auMosdBOe = models.CharField(max_length=3, blank=True, null=True, verbose_name='dB')
    auDisPoOe = models.CharField(max_length=3, blank=True, null=True, verbose_name='%')
    auDisdBOe = models.CharField(max_length=3, blank=True, null=True, verbose_name='dB')
    auSTROe = models.CharField(max_length=3, blank=True, null=True, verbose_name='dB')
    auLDVOe = models.CharField(max_length=3, blank=True, null=True, verbose_name='dB')
    auMascOe = models.CharField(max_length=3, blank=True, null=True, verbose_name='dB')
    auSpaceOe = models.CharField(max_length=3, blank=True, null=True, verbose_name='dB')
    auMosPoOd = models.CharField(max_length=3, blank=True, null=True, verbose_name='%')
    auMosdBOd = models.CharField(max_length=3, blank=True, null=True, verbose_name='dB')
    auDisPoOd = models.CharField(max_length=3, blank=True, null=True, verbose_name='%')
    auDisdBOd = models.CharField(max_length=3, blank=True, null=True, verbose_name='dB')
    auSTROd = models.CharField(max_length=3, blank=True, null=True, verbose_name='dB')
    auLDVOd = models.CharField(max_length=3, blank=True, null=True, verbose_name='dB')
    auMascOd = models.CharField(max_length=3, blank=True, null=True, verbose_name='dB')
    auSpaceOd = models.CharField(max_length=3, blank=True, null=True, verbose_name='dB')
    auObser = models.TextField(blank=True, null=True, verbose_name='Observações')

    def __str__(self) -> str:
        return f'{self.id} Data: {self.auData} Cliente: {self.aClient}'
    
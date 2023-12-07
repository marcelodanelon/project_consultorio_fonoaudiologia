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
    aConhece = models.CharField(max_length=50, null=True, blank=True, verbose_name='Onde conheceu a MARKI?')
    aDifiEsc = models.CharField(max_length=50, null=True, blank=True, verbose_name='Tem dificuldade para escutar?')
    aDifiPio = models.CharField(max_length=50, null=True, blank=True, verbose_name='Sua dificuldade está piorando?')
    aOuviMel = models.CharField(max_length=50, null=True, blank=True, verbose_name='Tem algum ouvido que escuta melhor?')
    aPessFam = models.CharField(max_length=50, null=True, blank=True, verbose_name='Há pessoas na sua família com perda de Audição?')
    aTrabRui = models.CharField(max_length=50, null=True, blank=True, verbose_name='Já trabalhou em Ambiente Ruidoso?')
    aTelevis = models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Televisão')
    aTeleFix = models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Telefone Fixo')
    aTeleCel = models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Celular')
    aConvGru = models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Conversa com grupo de pessoas')
    aConvRui = models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Conversa em ambiente ruidoso')
    aFalaBai = models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Fala muito baixa')
    aFaladis = models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Fala à distância')
    aCineTea = models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Cinema / Teatro')
    aPaleSal = models.BooleanField(blank=True, default=False, verbose_name='(Dificuldades) Palestra / Sala de aula')
    aOutrDif = models.CharField(max_length=50, null=True, blank=True, verbose_name='(Dificuldades) Outras')
    aZumbido = models.BooleanField(blank=True, default=False, verbose_name='(Percepções) Zumbido')
    aCoceira = models.BooleanField(blank=True, default=False, verbose_name='(Percepções) Coceira')
    aOtiteOO = models.BooleanField(blank=True, default=False, verbose_name='(Percepções) Otite')
    aDorOOOO = models.BooleanField(blank=True, default=False, verbose_name='(Percepções) Dor')
    aCiruOuv = models.BooleanField(blank=True, default=False, verbose_name='(Percepções) Cirurgia nos ouvidos')
    aTimpPer = models.BooleanField(blank=True, default=False, verbose_name='(Percepções) Tímpano perfurado')
    aSensTam = models.BooleanField(blank=True, default=False, verbose_name='(Percepções) Sensação de ouvido tampado')
    aOutrOuv = models.CharField(max_length=50, null=True, blank=True, verbose_name='(Percepções) Outros')
    aCardiop = models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Cardiopatia (problema de coração)')
    aPresAlt = models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Pressão Alta')
    aProbRin = models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Problemas nos rins')
    aTontura = models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Tonturas')
    aDiabete = models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Diabetes')
    aProbTir = models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Problema na Tireoide')
    aUsoOtot = models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Uso de ototóxico (antibiótico forte)')
    aColeAlt = models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Colesterol Alto')
    aLabirin = models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Labirintite')
    aCancerO = models.BooleanField(blank=True, default=False, verbose_name='(Doenças) Câncer')
    aOutrDoe = models.CharField(max_length=50, null=True, blank=True, verbose_name='(Doenças) Outras')
    aJaUsoAp = models.CharField(max_length=5, choices=[('sim', 'Sim'), ('não', 'Não')], null=True, blank=True, verbose_name='Já usou aparelho antes?')
    aMarcaOO = models.CharField(max_length=50, null=True, blank=True, verbose_name='Marca / Modelo Aparelho')
    aTempoOO = models.CharField(max_length=50, null=True, blank=True, verbose_name='Tempo de uso aparelho')
    aJaTesAp = models.CharField(max_length=5, choices=[('sim', 'Sim'), ('não', 'Não')], null=True, blank=True, verbose_name='Já testou aparelho?')
    aQualApa = models.CharField(max_length=50, null=True, blank=True, verbose_name='Qual aparelho já testou?')
    aApaIndi = models.CharField(max_length=50, null=True, blank=True, verbose_name='Aparelho Indicado')
    aValApar = models.CharField(max_length=50, null=True, blank=True, verbose_name='Valor aparelho')
    aLadoInd = models.CharField(max_length=50, choices=CHOICES_OUVIDO, null=True, blank=True, verbose_name='Lado Indicado')
    aFormPag = models.CharField(max_length=50, null=True, blank=True, verbose_name='Forma de Pagamento')
    aSaiTest = models.DateField(blank=True, null=True, verbose_name='Data de Saída para teste')
    aRetTest = models.DateField(blank=True, null=True, verbose_name='Data de Retorno de teste')
    aComClik = models.CharField(max_length=5, choices=[('sim', 'Sim'), ('não', 'Não')], null=True, blank=True, verbose_name='c/ Click')
    aSemClik = models.CharField(max_length=5, choices=[('sim', 'Sim'), ('não', 'Não')], null=True, blank=True, verbose_name='s/ click')
    aClikOOD = models.CharField(max_length=50, null=True, blank=True, verbose_name='Click Ouvido Direito')
    aClikOOE = models.CharField(max_length=50, null=True, blank=True, verbose_name='Click Ouvido Esquerdo')
    aTuboOOD = models.CharField(max_length=50, null=True, blank=True, verbose_name='Tubo Ouvido Direito')
    aTuboOOE = models.CharField(max_length=50, null=True, blank=True, verbose_name='Tubo Ouvido Esquerdo')
    aReceOOD = models.CharField(max_length=50, null=True, blank=True, verbose_name='Receptor Ouvido Direito')
    aReceOOE = models.CharField(max_length=50, null=True, blank=True, verbose_name='Receptor Ouvido Esquerdo')

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
    auCoordenadas_planoI_Linha1 = models.CharField(max_length=50, blank=True, null=True)
    auCoordenadas_planoI_Linha2 = models.CharField(max_length=50, blank=True, null=True)
    auCoordenadas_planoII_Linha1 = models.CharField(max_length=50, blank=True, null=True)
    auCoordenadas_planoII_Linha2 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.id} Data: {self.auData} Cliente: {self.aClient}'
    
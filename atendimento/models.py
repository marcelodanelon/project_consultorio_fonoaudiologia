from django.db import models
from home.models import ClientModel, ProfessionalModel, LocalModel

CHOICES_OUVIDO = [
    ("OE" ,"Ouvido Esquerdo"),
    ("OD" ,"Ouvido Direito"),
    ("Ambos" ,"Ambos"),
]

class AtendimentoModel(models.Model):
    aClient = models.ForeignKey(ClientModel, verbose_name="Cliente", on_delete=models.SET_NULL, null=True)
    aProfessional = models.ForeignKey(ProfessionalModel, verbose_name="Profissional", on_delete=models.SET_NULL, null=True)
    aLocal = models.ForeignKey(LocalModel, verbose_name="Unidade de Atendimento", on_delete=models.SET_NULL, null=True)
    aDataOOO = models.DateField(verbose_name="Data")
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
    aSituaca = models.CharField(max_length=15, choices=[('Em Andamento', 'Em Andamento'), ('Concluído', 'Concluído')], null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.data} {self.client}'
from atendimento.models import AtendimentoModel, AnamneseModel, ContatosTelefonicosModel, AudiometriaModel
from django import forms

class AtendimentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['aClient'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aProfessional'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aLocal'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aDemanda'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aDataPri'].widget.attrs.update({
            'class':'form-control mask-date',
        })
        self.fields['aConhece'].label = 'Onde conheceu a MARKI?'
        self.fields['aConhece'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aDifiEsc'].label = 'Tem dificuldade para escutar? Há quanto tempo? Sabe a causa?'
        self.fields['aDifiEsc'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aDifiPio'].label = 'Sua dificuldade está piorando?'
        self.fields['aDifiPio'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aOuviMel'].label = 'Tem algum ouvido que escuta melhor?'
        self.fields['aOuviMel'].widget.attrs.update({
            'class':'form-control dropdown',
        })
        self.fields['aPessFam'].label = 'Há pessoas na família com perda de audição?'
        self.fields['aPessFam'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aTrabRui'].label = 'Já trabalhou em ambiente ruidoso? Por quanto tempo?'
        self.fields['aTrabRui'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aObsAten'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aTelevis'].label = 'Televisão'
        self.fields['aTelevis'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aTeleFix'].label = 'Telefone fixo'
        self.fields['aTeleFix'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aTeleCel'].label = 'Celular'
        self.fields['aTeleCel'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aConvGru'].label = 'Conversa com grupo de pessoas'
        self.fields['aConvGru'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aConvRui'].label = 'Conversa em ambiente ruidoso'
        self.fields['aConvRui'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aFalaBai'].label = 'Fala muito baixa'
        self.fields['aFalaBai'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aFaladis'].label = 'Fala a distância'
        self.fields['aFaladis'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aCineTea'].label = 'Cinema/teatro'
        self.fields['aCineTea'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aPaleSal'].label = 'Palestra/sala de aula'
        self.fields['aPaleSal'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aOutrDif'].label = 'Outros'
        self.fields['aOutrDif'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aZumbido'].label = 'Zumbido'
        self.fields['aZumbido'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aCoceira'].label = 'Coceira'
        self.fields['aCoceira'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aOtiteOO'].label = 'Otite'
        self.fields['aOtiteOO'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aDorOOOO'].label = 'Dor'
        self.fields['aDorOOOO'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aCiruOuv'].label = 'Cirurgia nos ouvidos'
        self.fields['aCiruOuv'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aTimpPer'].label = 'Tímpano perfurado'
        self.fields['aTimpPer'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aSensTam'].label = 'Sensação de ouvido tampado'
        self.fields['aSensTam'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aOutrOuv'].label = 'Outros'
        self.fields['aOutrOuv'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aCardiop'].label = 'Cardiopatia(problema de coração)'
        self.fields['aCardiop'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aPresAlt'].label = 'Pressão Alta'
        self.fields['aPresAlt'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aProbRin'].label = 'Problemas nos rins'
        self.fields['aProbRin'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aTontura'].label = 'Tontura'
        self.fields['aTontura'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aDiabete'].label = 'Diabetes'
        self.fields['aDiabete'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aProbTir'].label = 'Problema na tireoide'
        self.fields['aProbTir'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aUsoOtot'].label = 'Uso de ototóxico(antibiótico forte)'
        self.fields['aUsoOtot'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aColeAlt'].label = 'Colesterol alto'
        self.fields['aColeAlt'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aLabirin'].label = 'Labirintite'
        self.fields['aLabirin'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aCancerO'].label = 'Câncer'
        self.fields['aCancerO'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['aOutrDoe'].label = 'Outros'
        self.fields['aOutrDoe'].widget.attrs.update({
            'class':'form-control',
        })

        self.fields['aJaUsoAp'].label = 'Já usou aparelho auditivo anteriormente?'
        self.fields['aJaUsoAp'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aMarcaOO'].label = 'Marca'
        self.fields['aMarcaOO'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aTempoOO'].label = 'Quanto Tempo?'
        self.fields['aTempoOO'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aJaTesAp'].label = 'Já testou o aparelho?'
        self.fields['aJaTesAp'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aQualApa'].label = 'Qual?'
        self.fields['aQualApa'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aApaIndi'].label = 'Aparelho Indicado'
        self.fields['aApaIndi'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aValApar'].label = 'Valor'
        self.fields['aValApar'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aLadoInd'].label = 'Lado Indicado'
        self.fields['aLadoInd'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aFormPag'].label = 'Forma PGTO'
        self.fields['aFormPag'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aSaiTest'].label = 'Data de Saída para teste'
        self.fields['aSaiTest'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aRetTest'].label = 'Data de retorno de teste'
        self.fields['aRetTest'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aComClik'].label = 'c/click'
        self.fields['aComClik'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aSemClik'].label = 's/click'
        self.fields['aSemClik'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aClikOOD'].label = 'OD'
        self.fields['aClikOOD'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aClikOOE'].label = 'OE'
        self.fields['aClikOOE'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aTuboOOD'].label = 'OD'
        self.fields['aTuboOOD'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aTuboOOE'].label = 'OE'
        self.fields['aTuboOOE'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aReceOOD'].label = 'OD'
        self.fields['aReceOOD'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aReceOOE'].label = 'OE'
        self.fields['aReceOOE'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aSituaca'].label = 'Situação'
        self.fields['aSituaca'].widget.attrs.update({
            'class':'form-control',
        })

    class Meta:
        model = AtendimentoModel
        fields = ('aClient', 'aProfessional', 'aLocal', 'aDemanda', 'aDataPri', 'aConhece', 
                  'aDifiEsc', 'aDifiPio', 'aOuviMel','aPessFam', 'aTrabRui', 'aObsAten', 
                  'aTelevis', 'aTeleFix', 'aTeleCel','aConvGru', 'aConvRui', 
                  'aFalaBai', 'aFaladis', 'aCineTea','aPaleSal', 'aOutrDif',
                  'aZumbido', 'aCoceira', 'aOtiteOO','aDorOOOO', 'aCiruOuv', 
                  'aTimpPer', 'aSensTam', 'aOutrOuv', 'aCardiop', 'aPresAlt',
                  'aProbRin', 'aTontura', 'aDiabete', 'aProbTir', 'aUsoOtot',
                  'aColeAlt', 'aLabirin', 'aCancerO', 'aOutrDoe', 'aJaUsoAp',
                  'aMarcaOO', 'aTempoOO', 'aJaTesAp', 'aQualApa', 'aApaIndi',
                  'aValApar', 'aLadoInd', 'aFormPag', 'aSaiTest', 'aRetTest',
                  'aComClik', 'aSemClik', 'aClikOOD', 'aClikOOE', 'aTuboOOD', 
                  'aTuboOOE', 'aReceOOD', 'aReceOOE', 'aSituaca')

class ContatosTelefonicosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['aTelData'].widget.attrs.update({
            'class':'form-control mask-date',
            'required': True,
        })
        self.fields['aTelLiga'].widget.attrs.update({
            'class':'form-control mask-telefone',
            'required': True,
        })
        self.fields['aTelObse'].widget.attrs.update({
            'class':'form-control',
        })

    class Meta:
        model = ContatosTelefonicosModel
        fields = ('aTelData', 'aTelLiga', 'aTelObse')

class AnamneseForm(forms.ModelForm):
    aAObserv = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['aDataAna'].label = 'Data:'
        self.fields['aDataAna'].widget.attrs.update({
            'class':'form-control mask-date',
        })
        self.fields['aAjustOD'].label = 'Ajuste OD:'
        self.fields['aAjustOD'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aAjustOE'].label = 'Ajuste OE:'
        self.fields['aAjustOE'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aAObserv'].label = 'Observações:'
        self.fields['aAObserv'].widget.attrs.update({
            'class':'form-control',
        })
    
    class Meta:
        model = AnamneseModel
        fields = ('aDataAna', 'aAjustOD', 'aAjustOE', 'aAObserv')

class AudiometriaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['aClient'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auData'].widget.attrs.update({
            'class':'form-control mask-date',
        })
        self.fields['auProfessional'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auLocal'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auAudio'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auCalib'].widget.attrs.update({
            'class':'form-control mask-date',
        })
        self.fields['auMedSo'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auMVaOe'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auMVoOe'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auMVaOd'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auMVoOd'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auMosPoOe'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auMosdBOe'].widget.attrs.update({
            'class':'form-control',
        })        
        self.fields['auDisPoOe'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auDisdBOe'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auSTROe'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auLDVOe'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auMascOe'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auSpaceOe'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auMosPoOd'].widget.attrs.update({
            'class':'form-control',
        })        
        self.fields['auMosdBOd'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auDisPoOd'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auDisdBOd'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auSTROd'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auLDVOd'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auMascOd'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auSpaceOd'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['auObser'].widget.attrs.update({
            'class':'form-control',
        })

    class Meta:
        model = AudiometriaModel
        fields = ('aClient','auData','auProfessional','auLocal',
                  'auAudio','auCalib','auMedSo','auMVaOe','auMVoOe',
                  'auMVaOd','auMVoOd','auMosPoOe','auMosdBOe','auDisPoOe',
                  'auDisdBOe','auSTROe','auLDVOe','auMascOe','auSpaceOe',
                  'auMosPoOd','auMosdBOd','auDisPoOd','auDisdBOd','auSTROd',
                  'auLDVOd','auMascOd','auSpaceOd','auObser')
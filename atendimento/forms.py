from atendimento.models import AtendimentoModel
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
        self.fields['aDataOOO'].widget.attrs.update({
            'class':'form-control',
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

    class Meta:
        model = AtendimentoModel
        fields = ('aClient', 'aProfessional', 'aLocal','aDataOOO', 'aConhece', 
                  'aDifiEsc', 'aDifiPio', 'aOuviMel','aPessFam', 'aTrabRui', 
                  'aTelevis', 'aTeleFix', 'aTeleCel','aConvGru', 'aConvRui', 
                  'aFalaBai', 'aFaladis', 'aCineTea','aPaleSal', 'aOutrDif',
                  'aZumbido', 'aCoceira', 'aOtiteOO','aDorOOOO', 'aCiruOuv', 
                  'aTimpPer', 'aSensTam', 'aOutrOuv')
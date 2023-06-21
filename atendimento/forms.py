from atendimento.models import AtendimentoModel
from django import forms

class AtendimentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['client'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['data'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['conheceu'].label = 'Onde conheceu a MARKI?'
        self.fields['conheceu'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['question1'].label = 'Tem dificuldade para escutar? Há quanto tempo? Sabe a causa?'
        self.fields['question1'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['question2'].label = 'Sua dificuldade está piorando?'
        self.fields['question2'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['question3'].label = 'Tem algum ouvido que escuta melhor?'
        self.fields['question3'].widget.attrs.update({
            'class':'form-control dropdown',
        })
        self.fields['question4'].label = 'Há pessoas na família com perda de audição?'
        self.fields['question4'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['question5'].label = 'Já trabalhou em ambiente ruidoso? Por quanto tempo?'
        self.fields['question5'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['question6a'].label = 'Televisão'
        self.fields['question6a'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['question6b'].label = 'Telefone fixo'
        self.fields['question6b'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['question6c'].label = 'Celular'
        self.fields['question6c'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['question6d'].label = 'Conversa com grupo de pessoas'
        self.fields['question6d'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['question6e'].label = 'Conversa em ambiente ruidoso'
        self.fields['question6e'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['question6f'].label = 'Fala muito baixa'
        self.fields['question6f'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['question6g'].label = 'Fala a distância'
        self.fields['question6g'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['question6h'].label = 'Cinema/teatro'
        self.fields['question6h'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['question6i'].label = 'Palestra/sala de aula'
        self.fields['question6i'].widget.attrs.update({
            'class':'form-check-label',
        })
        self.fields['question6j'].label = 'Outros'
        self.fields['question6j'].widget.attrs.update({
            'class':'form-control',
        })

    class Meta:
        model = AtendimentoModel
        fields = ('client', 'data', 'conheceu', 'question1', 'question2', 'question3',
                 'question4', 'question5', 'question6a', 'question6b', 'question6c',
                 'question6d', 'question6e', 'question6f', 'question6g', 'question6h',
                 'question6i', 'question6j', 'question7a', 'question7b', 'question7c',
                 'question7d', 'question7e', 'question7f', 'question7g', 'question7h')
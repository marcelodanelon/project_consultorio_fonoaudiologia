from django import forms
from estoque.models import InsumoModel, ItensInsumoModel, MovimentacaoInsumoModel
from datetime import date

class InsumoForm(forms.ModelForm):
    valor = forms.FloatField(disabled = True, required=False)
    quantidade = forms.IntegerField(disabled = True, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['descricao'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['valor'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['quantidade'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['marca'].widget.attrs.update({
            'class':'form-control dropdown',
        })
        self.fields['situacao'].widget.attrs.update({
            'class':'form-check-label',
        })

    class Meta:
        model = InsumoModel
        fields = '__all__'

class ItemInsumoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['insumo'].widget.attrs.update({
            'class': 'form-control',
            'required': True,
        })
        self.fields['valorUnitario'].widget.attrs.update({
            'class': 'form-control mask-money',
            'required': True,
        })
        self.fields['valorTotal'].widget.attrs.update({
            'class': 'form-control',
            'disabled': True,
        })
        self.fields['quantidade'].widget.attrs.update({
            'class': 'form-control',
            'required': True,
        })
        self.fields['dataValidade'].widget.attrs.update({
            'class': 'form-control mask-date',
        })
        self.fields['serie'].widget.attrs.update({
            'class': 'form-control',
        })

    class Meta:
        model = ItensInsumoModel
        fields = '__all__'

class MovimentacaoInsumoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['data'].widget.attrs.update({
            'class': 'form-control mask-date',
        })
        self.fields['local'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['operacao'].widget.attrs.update({
            'class': 'form-control',
        })

    class Meta:
        model = MovimentacaoInsumoModel
        fields = ('local','data','operacao')
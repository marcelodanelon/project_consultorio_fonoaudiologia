from django import forms
from estoque.models import InsumoModel, ItensInsumoModel, MovimentacaoInsumoModel

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
        })
        self.fields['valorUnitario'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['valorTotal'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['quantidade'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['dataValidade'].widget.attrs.update({
            'class': 'form-control',
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
            'class': 'form-control',
        })
        self.fields['unidade'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['operacao'].widget.attrs.update({
            'class': 'form-control',
        })

    class Meta:
        model = MovimentacaoInsumoModel
        fields = ('unidade','data','operacao')
from django import forms
from estoque.models import InsumoModel, ItensInsumoModel, ItensMovimentacaoInsumoModel, MovimentacaoInsumoModel, GrupoInsumoModel

class InsumoForm(forms.ModelForm):
    valor = forms.CharField(disabled = True, required=False)
    quantidade = forms.CharField(disabled = True, required=False)

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
        self.fields['grupoInsumo'].widget.attrs.update({
            'class':'form-control dropdown',
        })
        self.fields['controle'].widget.attrs.update({
            'class':'form-control dropdown',
        })
        self.fields['situacao'].widget.attrs.update({
            'class':'form-control dropdown',
        })

    class Meta:
        model = InsumoModel
        fields = '__all__'

class GrupoInsumoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['descricao'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['controleDeCompra'].widget.attrs.update({
            'class':'form-control',
        })

    class Meta:
        model = GrupoInsumoModel
        fields = ('descricao', 'controleDeCompra',)

class ItensInsumoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['insumo'].widget.attrs.update({
            'class': 'form-control',
            'required': True,
        })
        self.fields['valorUnitario'].widget.attrs.update({
            'class': 'form-control mask-money',
            'required': True,
            'value': '0,00',
            'min': "0",
        })
        self.fields['valorTotal'].widget.attrs.update({
            'class': 'form-control',
            'readonly': True,
            'value': '0,00',
            'min': "0",
        })
        self.fields['quantidade'].widget.attrs.update({
            'class': 'form-control',
            'required': True,
            'oninput': 'this.value = Math.round(this.value);',
            'min': "0",
        })
        self.fields['dataValidade'].widget.attrs.update({
            'class': 'form-control mask-date',
        })
        self.fields['serie'].widget.attrs.update({
            'class': 'form-control',
            'required': True,
        })

    class Meta:
        model = ItensInsumoModel
        fields = '__all__'

class ItensMovimentacaoInsumoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['insumo'].widget.attrs.update({
            'class': 'form-control',
            'required': True,
        })
        self.fields['valorUnitario'].widget.attrs.update({
            'class': 'form-control mask-money',
            'required': True,
            'value': '0,00',
            'min': "0",
        })
        self.fields['valorCompra'].widget.attrs.update({
            'class': 'form-control mask-money',
            'required': True,
            'value': '0,00',
            'min': "0",
        })
        self.fields['valorTotal'].widget.attrs.update({
            'class': 'form-control',
            'readonly': True,
            'value': '0,00',
            'min': "0",
        })
        self.fields['quantidade'].widget.attrs.update({
            'class': 'form-control',
            'required': True,
            'oninput': 'this.value = Math.round(this.value);',
            'min': "0",
        })
        self.fields['dataValidade'].widget.attrs.update({
            'class': 'form-control mask-date',
        })
        self.fields['serie'].widget.attrs.update({
            'class': 'form-control',
            'required': True,
        })

    class Meta:
        model = ItensMovimentacaoInsumoModel
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
        fields = ('operacao','local','data')
from django import forms
from estoque.models import InsumoModel

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

    class Meta:
        model = InsumoModel
        fields = ('descricao', 'valor', 'quantidade')


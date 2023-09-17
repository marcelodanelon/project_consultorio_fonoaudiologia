# forms.py
from django import forms
from estoque.models import ItensMovimentacaoInsumoModel

class RelatorioForm(forms.Form):
    campos = forms.MultipleChoiceField(
        choices=[(field.name, field.verbose_name) for field in ItensMovimentacaoInsumoModel._meta.get_fields()],
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    campos_agrupamento = forms.MultipleChoiceField(
        choices=[(field.name, field.verbose_name) for field in ItensMovimentacaoInsumoModel._meta.get_fields()],
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    campo_filtro = forms.ChoiceField(
        choices=[(field.name, field.verbose_name) for field in ItensMovimentacaoInsumoModel._meta.get_fields()],
        required=False,
    )

    filtro_valor = forms.CharField(max_length=100, required=False)


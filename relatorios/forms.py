# # forms.py
# from django import forms
# from estoque.models import ItensMovimentacaoInsumoModel

# class RelatorioForm(forms.Form):
#     campos = forms.MultipleChoiceField(
#         choices=[(field.name, field.verbose_name) for field in ItensMovimentacaoInsumoModel._meta.get_fields()],
#         widget=forms.CheckboxSelectMultiple,
#     )

# forms.py
from django import forms
from estoque.models import ItensMovimentacaoInsumoModel

class RelatorioForm(forms.Form):
    campos = forms.MultipleChoiceField(
        choices=[(field.name, field.verbose_name) for field in ItensMovimentacaoInsumoModel._meta.get_fields()],
        widget=forms.CheckboxSelectMultiple,
    )

    campos_agrupamento = forms.MultipleChoiceField(
        choices=[(field.name, field.verbose_name) for field in ItensMovimentacaoInsumoModel._meta.get_fields()],
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

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

# codigo para restringir fields
# campos_incluidos = ['campo1', 'campo2', 'campo3']

# class SeuForm(forms.Form):
#     campo_filtro = forms.ChoiceField(
#         choices=[
#             (field.name, field.verbose_name)
#             for field in ItensMovimentacaoInsumoModel._meta.get_fields()
#             if field.name in campos_incluidos  # Verifica se o nome do campo está na lista de campos incluídos
#         ],
#         required=False,
#     )
# forms.py
from django import forms
from django.db import models
from estoque.models import ItensMovimentacaoInsumoModel, MovimentacaoInsumoModel

campos_incluidos = ['operacao']

class RelatorioForm(forms.Form):
    campos = forms.MultipleChoiceField(
        choices=[(field.name, field.verbose_name) for field in ItensMovimentacaoInsumoModel._meta.get_fields()] + 
        [(field.name, field.verbose_name) for field in MovimentacaoInsumoModel._meta.get_fields()
          if isinstance(field, models.Field) and hasattr(field, 'verbose_name') and field.name in campos_incluidos],
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    campos_agrupamento = forms.ChoiceField(
        choices=[(field.name, field.verbose_name) for field in ItensMovimentacaoInsumoModel._meta.get_fields()] + 
        [(field.name, field.verbose_name) for field in MovimentacaoInsumoModel._meta.get_fields()
          if isinstance(field, models.Field) and hasattr(field, 'verbose_name') and field.name in campos_incluidos],
        widget=forms.Select(attrs={'class': 'form-control','style': 'font-size: 18px;'}),
        required=False,
    )

    campo_filtro = forms.ChoiceField(
        choices=[(field.name, field.verbose_name) for field in ItensMovimentacaoInsumoModel._meta.get_fields()]+ 
        [(field.name, field.verbose_name) for field in MovimentacaoInsumoModel._meta.get_fields()
          if isinstance(field, models.Field) and hasattr(field, 'verbose_name') and field.name in campos_incluidos],
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
    )

    filtro_valor = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

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
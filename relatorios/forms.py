# forms.py
from django import forms
from django.db import models
from estoque.models import ItensMovimentacaoInsumoModel, MovimentacaoInsumoModel
from atendimento.models import AtendimentoModel

campos_incluidos = ['operacao']

class RelatorioForm_MovimentacaoInsumos(forms.Form):
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

from django.utils.text import capfirst

def get_fields_with_verbose_name(model):
    fields_with_verbose_name = []
    for field in model._meta.get_fields():
        verbose_name = getattr(field, 'verbose_name', None)
        if verbose_name is not None and verbose_name != field.name:
            fields_with_verbose_name.append((field.name, verbose_name))
    return fields_with_verbose_name

class RelatorioForm_Atendimentos(forms.Form):
    model_fields = AtendimentoModel._meta.get_fields()

    campos = forms.MultipleChoiceField(
        choices=get_fields_with_verbose_name(AtendimentoModel),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    campos_agrupamento = forms.ChoiceField(
        choices=get_fields_with_verbose_name(AtendimentoModel),
        widget=forms.Select(attrs={'class': 'form-control', 'style': 'font-size: 18px;'}),
        required=False,
    )

    campo_filtro = forms.ChoiceField(
        choices=get_fields_with_verbose_name(AtendimentoModel),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
    )

    filtro_valor = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
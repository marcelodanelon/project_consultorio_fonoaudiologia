from django import forms
from agendamento.models import AgendamentoModel, AgendaModel

class AgendaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['aProfessional'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['aLocal'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['agDatIni'].widget.attrs.update({
            'class':'form-control mask-date',
        })
        self.fields['agDatFim'].widget.attrs.update({
            'class':'form-control mask-date',
        })
        self.fields['agHorIni'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['agHorFim'].widget.attrs.update({
            'class':'form-control mask-date',
        })
        self.fields['agTipAge'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['agQtdTot'].widget.attrs.update({
            'class':'form-control mask-date',
        })
        self.fields['agQtdTem'].widget.attrs.update({
            'class':'form-control',
        })

    class Meta:
        model = AgendaModel
        fields = '__all__'
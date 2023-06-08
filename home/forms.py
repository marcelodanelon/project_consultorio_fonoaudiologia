from django import forms
from home.models import ClientModel
from django.core.exceptions import ValidationError

class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['last_name'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['born'].widget.attrs.update({
            'class':'form-control',
            'placeholder': 'dd/mm/yyyy',
        })
        self.fields['responsibleName'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['responsiblePhone'].widget.attrs.update({
            'class':'form-control',
            'placeholder': '(00)00000-0000',
        })
        self.fields['street'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['district'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['number'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['city'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['state'].widget.attrs.update({
            'class':'form-control dropdown',
        })
        self.fields['zipcode'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['complement'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['document1'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['document2'].widget.attrs.update({
            'class':'form-control',
        })
        self.fields['phone1'].widget.attrs.update({
            'class':'form-control',
            'placeholder': '(00)00000-0000',
        })
        self.fields['phone2'].widget.attrs.update({
            'class':'form-control',
            'placeholder': '(00)00000-0000',
        })
        self.fields['status'].widget.attrs.update({
            'class':'form-control',
        })

    class Meta:
        model = ClientModel
        fields = ('first_name', 'last_name', 'born', 'responsibleName', 'responsiblePhone',
                'street', 'district', 'number', 'city', 'state', 'zipcode', 'complement',
                'document1', 'document2', 'phone1', 'phone2','status',
                )
        
        # error_messages = {
        #     'task': {
        #         'max_length': ("Error: maximum length limit is 255 characters"),
                
        #     },
        # }
    # def clean_name(self):
    #     cleaned_data = self.cleaned_data.get('first_name')

    #     if cleaned_data == 'MARCELO':
    #         raise ValidationError(
    #             'Digite outro nome',
    #             code='invalid'
    #         )

    #     return cleaned_data
    
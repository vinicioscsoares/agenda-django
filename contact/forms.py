from django import forms
from django.core.exceptions import ValidationError

from . import models

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'digite seu texto aqui',
            }
        ),
        label='Primeiro nome',
        help_text="texto de ajuda"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class':'classe-a classe-b',
        #     'placeholder':'digite aqui :)',   
        # })

    class Meta:
        model = models.Contact
        fields = ( 'first_name', 
        'last_name',
        'phone', 'email', 'description', 'category',
        ) 

        
        # widgets = { 
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class':'classe-a classe-b',
        #             'placeholder':'digite seu nome aqui :)' 
        #         }
        #     )
        # }

    def clean(self):

        cleaned_data = self.cleaned_data

        self.add_error(
            None,
            ValidationError(
                'Deu erro, amigo.',
                code='invalid',

            )
        )
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        
        if first_name == 'ABC':
          self.add_error(
            'first_name',ValidationError(
                "veio do add_error",
                code='invalid'
            )
          )
        return first_name
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
    
        return last_name
    def clean(self):

        cleaned_data = super().clean()

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name and last_name and first_name == last_name:
            self.add_error(
                'last_name', ValidationError(
                    "last name não pode ser igual ao first_name", code= 'invalid'
                )
            )
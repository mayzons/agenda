from django import forms
from django.core.exceptions import ValidationError

from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TimeInput(
            attrs={
                'class': 'classe-a classe-b',
                'pleaceholder': 'Escrava aqui',
                }
            ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

        # self.fields['first_name'].widget.attrs.update(
        #     {'class': 'classe-a classe-b',
        #      'pleaceholder': 'Escrava aqui'}
        # )

    class Meta:
        model = models.Contact
        fields = (
             'first_name', 'last_name', 'phone',
        )
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'pleaceholder': 'Escrava aqui'
        #         }
        #     )
        # }

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
         )
        self.add_error(
            'first_name',
            ValidationError(
                 'Mensagem de erro 2',
                 code='invalid'
             )
         )

        return super().clean()

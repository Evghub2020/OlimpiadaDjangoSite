from .models import Participants
from django.forms import EmailInput, ModelForm, TextInput


class ParticipantsForm(ModelForm):
    class Meta:
        model = Participants
        fields = ['name','title_univer','phone','email' ]


        widgets = {
            "name": TextInput(attrs={
                'class': 'form-input__input',
                'placeholder': 'Иванов Иван Иванович'
            }),
            "title_univer": TextInput(attrs={
                'class': 'form-input__input',
                'placeholder': 'РГЭУ (РИНХ)'
            }),
            "phone": TextInput(attrs={
                'class': 'form-input__input',
                'placeholder': '+7 (___) ___-__-__'
            }),
            "email": EmailInput(attrs={
                'class': 'form-input__input',
                'placeholder': 'example@mail.ru'
            }),
        }
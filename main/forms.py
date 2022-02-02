from .models import Girl
from django.forms import ModelForm, TextInput, Textarea, NumberInput


class GirlForm(ModelForm):
    class Meta:
        model = Girl
        fields = ["title", "age", "descript"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "age": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите возраст'
            }),
            "descript": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }

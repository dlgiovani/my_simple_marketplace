from django import forms
from .models import Item
from django.utils.translation import gettext_lazy as _
from djmoney.forms.widgets import MoneyWidget

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'briefing', 'description', 'price', 'image_url',)

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'briefing': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            }),
            'price': MoneyWidget(attrs={
                'class': INPUT_CLASSES,
            }),
            'image_url': forms.FileInput(),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'briefing', 'description',
                  'price', 'image_url', 'is_sold')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'briefing': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            }),
            'price': MoneyWidget(attrs={
                'class': INPUT_CLASSES,
            }),
            'image_url': forms.FileInput(),
        }

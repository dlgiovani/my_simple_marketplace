from django import forms
from .models import Item
from django.utils.translation import gettext_lazy as _

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class PriceField(forms.FloatField):
    def to_python(self, value):
        if value:
            value = value.replace(',', '.')
        return super().to_python(value)

    def prepare_value(self, value):
        if value is not None:
            return str(value).replace('.', ',')
        return value


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image_url',)
        price = PriceField(label=_('Price'), help_text=_('Enter the price using either . or , as cents separator.'))

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'image_url': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description',
                  'price', 'image_url', 'is_sold')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'image_url': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
        }

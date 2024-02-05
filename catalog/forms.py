from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    FORBIDDEN = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'description', 'img', 'category', 'price', 'is_active',)

    def clean_name(self):
        cleaned_name = self.cleaned_data['name']
        for s in self.FORBIDDEN:
            if s.lower() in cleaned_name.lower():
                raise forms.ValidationError('Имя товара содержит недопустимые данные')
        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data['description']
        for s in self.FORBIDDEN:
            if s.lower() in cleaned_description.lower():
                raise forms.ValidationError('Описание товара содержит недопустимые данные')
        return cleaned_description

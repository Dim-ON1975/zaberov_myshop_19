from django import forms
from .models import Product, Version


class ProductForm(forms.ModelForm):
    FORBIDDEN = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'description', 'img', 'category', 'price', 'is_active', 'is_published', 'user',)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Извлекаем атрибут request
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()  # Скрываем поле user

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.request:
            instance.user = self.request.user  # Устанавливаем текущего пользователя в качестве автора
        if commit:
            instance.save()
        return instance

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


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_is_active(self):
        is_active = self.cleaned_data.get('is_active')
        all_active_versions = Version.objects.all().filter(product=self.cleaned_data.get('product')).filter(
            is_active=True)
        if len(all_active_versions) >= 1 and is_active:
            if len(all_active_versions.filter(num_version=self.cleaned_data.get('num_version'))) == 0:
                raise forms.ValidationError('Выберете только одну активную версию')
        return is_active

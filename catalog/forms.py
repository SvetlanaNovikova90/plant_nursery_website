from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class ProductForm(StyleMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image_ph', 'category', 'price')

    def clean_name(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        cleaned_data = self.cleaned_data['name']

        for i in forbidden_words:
            if i in cleaned_data:
                raise forms.ValidationError('Вы ввели запрещенное слово')
        return cleaned_data

    def clean_description(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        cleaned_data = self.cleaned_data['description']

        for i in forbidden_words:
            if i in cleaned_data:
                raise forms.ValidationError('Вы ввели запрещенное слово')
        return cleaned_data


class VersionForm(StyleMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

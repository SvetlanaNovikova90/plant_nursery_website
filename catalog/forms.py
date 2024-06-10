from django import forms


from catalog.models import Product, Version


class StyleMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name != 'current_version_indicator' and field_name != 'publication_sign' and field_name != 'is_published':

                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleMixin):
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


class ProductModeratorForm(StyleMixin):
    class Meta:
        model = Product
        fields = ('description', 'category')


class ProductIsPublishedForm(StyleMixin):

    class Meta:
        model = Product
        fields = ('is_published',)


class ProductDescriptionForm(StyleMixin):

    class Meta:
        model = Product
        fields = ('description',)


class ProductCategoryForm(StyleMixin):

    class Meta:
        model = Product
        fields = ('category',)


class VersionForm(StyleMixin):

    class Meta:
        model = Version
        fields = '__all__'

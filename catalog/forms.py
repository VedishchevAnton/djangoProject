from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']  # список запрещенных слов
        for word in forbidden_words:
            # Проверяем, содержит ли название или описание запрещенное слово
            if word in name.lower() or word in description.lower():
                # Если содержит, генерируем исключение с сообщением об ошибке
                raise forms.ValidationError(f'Слово "{word}" запрещено в названии и описании продукта.')
        return cleaned_data

# Валидация в Django - это процесс проверки данных, введенных пользователем, на соответствие заданным правилам. В
# Django валидация может быть выполнена на разных уровнях, например, на уровне форм, моделей или сериализаторов

from django import forms
from .models import Product
from .models import Stock


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price')

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 100:
            raise forms.ValidationError('価格は100円以上')

        return price

    def clean(self):
        price = self.cleaned_data['price']
        name = self.cleaned_data['name']
        if name == 'PC' and price < 10000:
            raise forms.ValidationError('PCは10000円以上')

        return self.cleaned_data

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'


class ProductForm2(forms.ModelForm):
    name = forms.CharField(label='商品名')
    price = forms.IntegerField(label='価格')

    class Meta:
        model = Product
        fields = ('name', 'price')

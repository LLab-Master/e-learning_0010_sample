from django import forms

class MemberForm(forms.Form):
    id = forms.CharField()
    name = forms.CharField(label='名前')
    age = forms.IntegerField(label='年齢')
    birthday = forms.DateField(label='誕生日')
    password = forms.CharField(widget=forms.PasswordInput)


class ProductForm(forms.Form):
    name = forms.CharField()
    price = forms.IntegerField()

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

        return cleaned_data

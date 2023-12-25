from django import forms
from .models import Member

class MyForm(forms.Form):
    age = forms.IntegerField(label='年齢')
    name = forms.ChoiceField(
            label='性別',
            choices=(
                (0, '未回答'),
                (1, '男'),
                (2, '女'),
            ),)
    text = forms.CharField(label='ご意見', widget=forms.Textarea)

class MemberCreateForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = "__all__"
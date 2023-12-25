from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from chapter04.forms import MemberForm

def show_forms(request):
    member_form = MemberForm()
    ctx = {'form': member_form, }

    return render(request, 'show_forms.html', ctx)


def create_member(request):
    ctx = {}    # コンテキスト
    if request.method == 'POST':    # POSTメソッド = Formからのsubmit
        form = MemberForm(request.POST)   # POST データからフォーム作成
        if form.is_valid(): # バリデーションOK
            ctx['new_member'] = {                # コンテキストに追加
                'id': form.cleaned_data.get('id'),
                'name': form.cleaned_data['name'],
                'age': form.cleaned_data['age'],
                'birthday': form.cleaned_data['birthday'],
                'password': form.cleaned_data['password'] ,}
            return render(request, 'confirm_member.html', ctx)
        else:   # バリデーション NG
            ctx['form'] = form
            ctx['msg'] = '入力エラーがあります'
            return render(request, 'create_member.html', ctx)
    else:    # POSTメソッド = 初回のアクセス
        form = MemberForm()   # 空のフォーム
        ctx['form'] = form
        return render(request, 'create_member.html', ctx)


class ShowFormView(generic.FormView):
    template_name = 'show_forms.html'
    form_class = MemberForm
    success_url = reverse_lazy('chapter04:ok')

class OkView(generic.TemplateView):
    template_name = 'ok.html'

from django.shortcuts import render

def set_session(request, param1):
    # データは URLパラメータでもらう
    request.session['param1'] = param1
    return render(request, 'set_session.html')

def view_session(request):
    # テンプレートからアクセス
    return render(request, 'view_session.html')

def get_session(request):
    # セッション->コンテキスト
    ctx = {'param1':request.session.get('param1')}
    request.session.pop('param1', None)    # 取り出し終わったセッションデータは削除
    return render(request, 'get_session.html', ctx)

from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


def template_sample(request):
    ctx = {
        'simple_var' : 'My car',
        'list_var' : [1, 5, 3, 2],
        'dic_var' : {
            'key1' : 'value1',
            'key2' : 'value2',
            'key3' : 'value3',
        },
    }

    return render(request, 'template_sample.html', ctx)


class TemplateSample(generic.TemplateView):
    template_name = 'template_sample.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['simple_var'] = 'My car'
        ctx['list_var']  = [1, 5, 3, 2]
        ctx['dic_var']  = {
            'key1' : 'value1',
            'key2' : 'value2',
            'key3' : 'value3',
        }

        return ctx


def param_from_form(request):
    if request.method == 'POST':
        v_name = request.POST['p_name']
        v_age = request.POST['p_age']
    else:
        v_name = request.GET['p_name']
        v_age = request.GET['p_age']

    ctx = {
        'name': v_name,
        'age': v_age, }

    return render(request, 'show_param.html', ctx)


def get_sample1(request):
    return render(request, 'get_sample1.html')

def post_sample1(request):
    return render(request, 'post_sample1.html')

def top_page3(request):
    return render(request, 'top3.html')

def top_page4(request):
    return render(request, 'top4.html')

def param_from_url(request, param1, param2):
    return render(request, 'select.html', {'param1':param1, 'param2':param2})

def zipcode(request, param1):
    return HttpResponse("あなたが選んだのは郵便番号です")


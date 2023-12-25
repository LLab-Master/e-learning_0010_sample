from django.urls import path, re_path
from . import views # アプリの views を import

app_name = 'chapter03'   # アプリの逆引き名

urlpatterns = [
    path('tmp_sample/', views.template_sample, name='tmp_smpl'),
    path('tmp_sample2/', views.TemplateSample.as_view(), name='tmp_smpl2'),
    path('get_sample1/', views.get_sample1, name='get_sample1'),
    path('post_sample1/', views.post_sample1, name='post_sample1'),
    path('param_from_form/', views.param_from_form, name='param_form'),
    path('select/<str:param1>/<str:param2>/', views.param_from_url, name='select'),
    re_path('regex/(?P<param1>[0-9]{3}-[0-9]{4})/', views.zipcode, name='zipcode'),
]

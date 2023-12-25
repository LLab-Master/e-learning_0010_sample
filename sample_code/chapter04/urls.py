from django.urls import path
from . import views

app_name = 'chapter04'

urlpatterns = [
    path('show_forms/', views.show_forms, name='show_forms'),
    path('show_forms_cls/', views.ShowFormView.as_view(), name='show_forms_cls'),
    path('create_member/', views.create_member, name='create_member'),
    path('ok/', views.OkView.as_view(), name='ok'),

]

from django.urls import path
from . import views

app_name = 'chapter05'

urlpatterns = [
    path('add_products/', views.add_products, name='add_products'),
    path('search_products1/', views.search_products1, name='search_products1'),
    path('search_products2/', views.search_products2, name='search_products2'),
    path('search_products3/', views.search_products3, name='search_products3'),
    path('search_products4/', views.search_products4, name='search_products4'),
    path('search_stock1/', views.search_stock1, name='search_stock1'),
    path('search_stock2/', views.search_stock2, name='search_stock2'),
    path('insert_product/', views.insert_product, name='insert_product'),
    path('insert_product_end/', views.insert_product_end, name='insert_product_end'),
    path('insert_stock/', views.insert_stock, name='insert_stock'),
    path('update_product/<int:pk>/', views.update_product, name='update_product'),
    path('update_product_end/', views.update_product_end, name='update_product_end'),
    path('insert_product2/', views.insert_product2, name='insert_product2'),
]

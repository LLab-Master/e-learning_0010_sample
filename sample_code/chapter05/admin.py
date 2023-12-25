from django.contrib import admin
# 下の 2 行を追加
from .models import Product
admin.site.register(Product)

from .models import Stock
admin.site.register(Stock)

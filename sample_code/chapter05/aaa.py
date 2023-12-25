from chapter05.models import Product
# 全部
products = Product.objects.all()
# nameで検索
qs1 = Product.objects.filter(name='ボールペン')
# price > 1000
qs2 = Product.objects.filter(price__gt=1000)
# name に'筆'を含む
qs3 = Product.objects.filter(name__contains='筆')
# 上の結果からpriceで絞り込み
qs4 = qs3.filter(price__gt=150)
# メソッドチェーンでも書ける
qs5 = Product.objects.filter(name__contains='筆').filter(price__gt=150)

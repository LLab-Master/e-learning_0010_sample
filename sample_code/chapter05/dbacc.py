from .models import Product

# レコード作成
pen = Product(name='pen', price=120)
cap = Product(name='cap', price=2000)
bag = Product(name='bag', price=3500)

# データベースへ格納
pen.save()
cap.save()
bag.save()

# 検索
products = Product.objects.all()                  # 全部

qs1 = Product.objects.filter(name='ボールペン')   # nameで検索
qs2 = Product.objects.filter(price__gt=1000)      # price > 1000

qs3 = Product.objects.filter(name__contains='筆') # name に'筆'を含む
qs4 = qs3.filter(price__gt=150)                   # 上の結果からpriceで絞り込み
qs5 = Product.objects
             .filter(name__contains='筆')
             .filter(price__gt=150)               # メソッドチェーンでも書ける



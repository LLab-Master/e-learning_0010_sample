from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Stock

def add_products(request):
    # 新規登録
    prod1 = Product(name='ボールペン', price=250)
    prod1.save()
    prod2 = Product(name='鉛筆', price=120)
    prod2.save()
    prod3 = Product(name='万年筆', price=5000)
    prod3.save()
    prod4 = Product(name='パン', price=150)
    prod4.save()

    # 更新
    prod1.price = 200
    prod1.save()

    # 削除
    prod4.delete()

    return HttpResponse('商品を登録しました')

def search_products1(request):
    # objects.all()
    qs1 = Product.objects.all()

    products = []
    for qs in qs1:
        products.append({'name':qs.name, 'price':qs.price})

    ctx = {
        'condition':'ALL',
        'products':products
    }
    return render(request, 'search_products.html', ctx)

def search_products2(request):
    # objects.filter()
    qs1 = Product.objects.filter(name='鉛筆')

    products = []
    for qs in qs1:
        products.append({'name':qs.name, 'price':qs.price})

    ctx = {
        'condition':'name=\'鉛筆\'',
        'products':products
    }
    return render(request, 'search_products.html', ctx)

def search_products3(request):
    qs1 = Product.objects.filter(price__range=(120,5000))

    products = []
    for qs in qs1:
        products.append({'name':qs.name, 'price':qs.price})

    ctx = {
        'condition':'100<price<1000',
        'products':products
    }
    return render(request, 'search_products.html', ctx)

from django.db.models import Q
def search_products4(request):
    # ANDはQオブジェクトを '&' でつなぐ 
    q_and1 = Q(price__gt=100) & Q(price__lt=1000)

    # ORはQオブジェクトを '|' でつなぐ 
    q_or1 = Q(price__lt=100) | Q(price__gt=1000)    

    # NOTはQオブジェクトの前に '~' を置く
    q_not = ~Q(price=5000)

    # add() を使った AND
    q_and2 = Q()
    q_and2.add(Q(price__gt=100), Q.AND)
    q_and2.add(Q(price__lt=1000), Q.AND)

    # add() を使った OR    
    q_or2 = Q()
    q_or2.add(Q(price__lt=100), Q.AND)
    q_or2.add(Q(price__gt=1000), Q.OR)

    qs1 = Product.objects.filter(q_and1)
    print(qs1)
    qs1 = Product.objects.filter(q_or1)
    print(qs1)
    qs1 = Product.objects.filter(q_and2)
    print(qs1)
    qs1 = Product.objects.filter(q_or2)
    print(qs1)
    qs1 = Product.objects.filter(q_not)
    print(qs1)

    return HttpResponse('OK')

from .forms import ProductForm, StockForm, ProductForm2

def insert_product(request):
    ctx = {'form': ProductForm()}   # 空のフォーム
    return render(request, 'insert_product.html', ctx)

def insert_product_end(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)   # POST データからフォーム作成
        if form.is_valid(): # バリデーションOK
            form.save()        # データベース登録
            message = '登録しました'
        else:
            message = '登録できませんでした'
    else:
        message = '登録できませんでした'

    return HttpResponse(message)

def insert_stock(request):
    ctx = {'form': StockForm()}   # 空のフォーム
    return render(request, 'insert_stock.html', ctx)

def insert_stock_end(request):
    if request.method == 'POST':
        form = StockForm(request.POST)   # POST データからフォーム作成
        if form.is_valid(): # バリデーションOK
            form.save()     #
            message = '登録しました'
        else:
            message = '登録できませんでした'
    else:
        message = '登録できませんでした'

    return HttpResponse(message)

def update_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except:
        return HttpResponse('<H1>指定されたIDは存在しません</H1>')

    form = ProductForm(instance=product)
    ctx = {'form':form}
    return render(request, 'update_product.html', ctx)

def update_product_end(request, pk):
    if request.method == 'POST':
        try:
            product = Product.objects.get(id=pk)
        except:
            return HttpResponse('<H1>指定されたIDは存在しません</H1>')

        form = ProductForm(request.POST, instance=product)
        if form.is_valid(): # バリデーションOK
            Product(
                name=form.cleaned_data.get('name'),
                price=form.cleaned_data.get('price'),
            ).save()        # データベース登録
    ctx = {'id':pk, 'form':form}
    return HttpResponse('<h3>更新終了</h3>')

def insert_product2(request):
    ctx = {'form': ProductForm2()}   # 空のフォーム
    return render(request, 'insert_product.html', ctx)

def app_top(request):
    return render(request, 'app_top.html')


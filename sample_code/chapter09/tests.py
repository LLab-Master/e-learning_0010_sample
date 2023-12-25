from django.test import TestCase

from .models import Product
from .forms import ProductForm

class ProductTest(TestCase):
    def create_test(self):
        Product(name='あんパン', price=150).save()
        Product(name='カレーパン', price=170).save()

        products = Product.objects.all()
        self.assertEqual(len(products), 2)
        self.assertEqual(products[0].name, 'あんパン')
        self.assertEqual(products[0].price, 150)
        self.assertEqual(products[1].name, 'カレーパン')
        self.assertEqual(products[1].price, 170)

class ProductFormTest(TestCase):
    def test_valid(self):
        params = {
            'name' : '食パン',
            'price' : 100,
        }
        form = ProductForm(params)
        self.assertTrue(form.is_valid())

    def test_invalid(self):
        params = {
            'name' : '食パン',
            'price' : 80,    # 価格が100円以上というカスタムバリデーションあり
        }
        form = ProductForm(params)
        self.assertFalse(form.is_valid())

from django.urls import reverse, resolve
from .views import app_top
from django.views import generic

class URLTest(TestCase):
    def test_top(self):
        url = reverse('chapter09:app_top')
        self.assertEqual(resolve(url).func, app_top)

    def test_home(self):
        url = reverse('chapter09:home')
        self.assertEqual(resolve(url).func.view_class, generic.TemplateView)

class ViewTest(TestCase):
    def test_get(self):
        response = self.client.get(reverse('chapter09:app_top'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'TOP')

    def test_post(self):
        response = self.client.post(
            reverse('chapter09:add'),
            data={
                'name':'あんパン',
                'price':'150',
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "登録しました")


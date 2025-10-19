from django.urls import path

from store.apps.products.views import ProductList

urlpatterns = [
    path('list/', ProductList.as_view(), name='product-list'),
]

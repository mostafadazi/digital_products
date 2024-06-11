
from products.views import ProductListView
from django.urls import path

urlpatterns = [
    path('products/',ProductListView.as_view()),
]
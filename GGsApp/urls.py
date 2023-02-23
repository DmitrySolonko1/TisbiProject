from django.urls import path, reverse_lazy
from .views import *


urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('product/<int:pk>/', ProductPage.as_view(), name='product_page'),
    path('add_product', AddProductPage.as_view(), name='add_product')


]

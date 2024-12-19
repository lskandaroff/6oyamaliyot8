from django.urls import path
from .views import home, about_products

urlpatterns = [
    path('', home, name="home"),
    path('product/<int:product_id>/', about_products, name='about_products')
]
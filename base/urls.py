from django.urls import path
from . import views
urlpatterns = [
    path('', views.getRequest,name="routes"),
    path('products/',views.getProducts, name="products"),
    path('product/<str:pk>',views.getProduct, name="product"),
]
from django.urls import path
from django.views.generic import TemplateView

from products import views

urlpatterns = [
    path('sell/', views.sell, name='sell'),
    path('buy/iphone/', views.product_list, name='iphone'),
    path('<slug:type_slug>/', views.list, name='product_list_by_type'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
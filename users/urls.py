from django.urls import path
from users import views

urlpatterns = [
    path('edit_me/', views.me, name='me'),
    path('my/profile/', views.profile, name='profile'),
]
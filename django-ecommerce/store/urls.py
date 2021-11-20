from django.urls import path
from . import views
from django.views.generic import TemplateView



urlpatterns=[
    path('', views.StoreView.as_view(), name="store"),
    path('cart/', views.CartView.as_view(), name="cart"),
    path('about/', views.About.as_view(), name="about"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('categories/', views.CategoryView.as_view(), name='categories'),
    path('category/<int:pk>/', views.SpecificCategory.as_view(), name='category'),
    path('product/<int:pk>/', views.ProductView.as_view(), name='product'),

]
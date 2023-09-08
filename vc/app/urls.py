from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register-as-vendor/', views.register_as_vendor_views, name='register_as_vendor'),
    path('register-as-distributor/', views.register_as_distributor_views, name='register_as_distributor'),
    path('search/', views.search_views, name='search'),
    path('profile/', views.profile, name='profile'),
    path('orders/', views.orders_view, name='orders'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
]   
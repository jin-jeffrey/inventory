"""invapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from users import views as user_views
from inventory import views as inventory_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('inventory/', inventory_views.ItemListView.as_view(), name = 'inventory'),
    path('item/<int:pk>/', inventory_views.ItemDetailView.as_view(), name = 'item-detail'),
    path('item/new/', inventory_views.ItemCreateView.as_view(), name = 'item-create'),
    path('item/<int:pk>/update/', inventory_views.ItemUpdateView.as_view(), name = 'item-update'),
    path('item/<int:pk>/delete/', inventory_views.ItemDeleteView.as_view(), name = 'item-delete'),
    path('', inventory_views.about, name = 'about')
]


from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('about/', views.about),
    path('posts/', include('posts.urls')),  # Ajoutez une virgule ici
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]



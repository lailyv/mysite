from django.urls import path
from . import views
 
urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('greeting/', views.formView, name='logged'),
    path('logout/', views.logoutView, name='logout'),
]
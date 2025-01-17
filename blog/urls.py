from django.urls import path
from .views import blogdetails, bloglist
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('',bloglist.as_view(), name='home1'),
    # path('blogss/', views.blogdetails.as_view, name='detai')
     path('bothh/', views.indexView, name='home'),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView, name="register_url"),
    path('logout/',LogoutView.as_view(next_page="home"), name="Logout"),
]


from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogdetails.as_view, name='home1'),
    # path('blogss/', views.blogdetails.as_view, name='detai')
]


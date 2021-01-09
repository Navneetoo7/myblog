from django.urls import path
from .views import blogdetails, bloglist

urlpatterns = [
    path('',bloglist.as_view(), name='home1'),
    # path('blogss/', views.blogdetails.as_view, name='detai')
]


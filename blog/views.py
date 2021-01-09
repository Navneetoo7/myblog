from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import mywebblog 
# Create your views here.


class bloglist(ListView):
    template_name = 'index.html'
    def getdetails(self):
        return mywebblog.objects.all()

class blogdetails(DetailView):
    model =mywebblog
    template_name = 'index.html'       
1

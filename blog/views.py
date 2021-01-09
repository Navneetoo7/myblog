from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import mywebblog 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


class bloglist(ListView):
    model =mywebblog
    template_name = 'check.html'
    # template_name = 'index.html'
    # def getdetails(self):
    #     return mywebblog.objects.all()

class blogdetails(DetailView):
    model =mywebblog
    template_name = 'index.html'  
    

    # _____for login___

def indexView(request):
    return render(request,'both.html')    
@login_required
def dashboardView(request):
    return render(request,'dashboard.html') 

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        else:
            form = UserCreationForm()
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})     


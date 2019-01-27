from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import logout
from .forms import RegisterForm
# Create your views here.

class RegisterView(CreateView):
    form_class=RegisterForm
    template_name='registration/register.html'
    success_url='/login/'


def home_view(request):
    return render(request,"base.html")



def logout_view(request):
    logout(request)
    return render(request,"registration/login.html")

from django.shortcuts import render
from django.views.generic import ListView
from .models import Passbook
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def home_view(request):
    return render(request,"registration/login.html")

#Listview
class PassbookListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    def get_queryset(self):
        return Passbook.objects.filter(owner=self.request.user)

        
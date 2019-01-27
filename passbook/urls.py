from django.urls import path
from passbook.views import(home_view,PassbookListView)

urlpatterns = [
    path('',home_view, name='home'),
    path('passbook/', PassbookListView.as_view(),name='passbook'),
]
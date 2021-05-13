from django.urls import path
from .views import HomePageView
#this defines urls patterns

urlpatterns = [
    path('', HomePageView.as_view(), name='home')
]

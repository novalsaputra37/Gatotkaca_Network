from django.urls import path
from .views import HomeView, AboutView, KostView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home-view'),
    path('kost/', KostView.as_view(), name='kost'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact')
    ]
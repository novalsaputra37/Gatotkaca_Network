from django.urls import path
from .views import HomeView, AboutView, KostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('kost/', KostView.as_view(), name='kost'),
    path('about/', AboutView.as_view(), name='about'),
    ]
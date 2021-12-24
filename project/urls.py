from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectKategoriListView

app_name = 'project'
urlpatterns = [
    path('', ProjectListView.as_view(), name='list'),
    path('detail/<slug>', ProjectDetailView.as_view(), name='detail'),
    path('kategori/<kategori>', ProjectKategoriListView.as_view(), name='kategori'),
    ]
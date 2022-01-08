from django.urls import path, re_path
from .views import ProjectListView, ProjectDetailView, ProjectKategoriListView

app_name = 'project'
urlpatterns = [
    path('<page>', ProjectListView.as_view(), name='list'),
    #re_path(r'^(?P<page>\d+)$', ProjectListView.as_view(), name='list'),
    path('detail/<slug>', ProjectDetailView.as_view(), name='detail'),
    path('kategori/<kategori>', ProjectKategoriListView.as_view(), name='kategori'),
    ]
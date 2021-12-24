from django.shortcuts import render
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView, 
	DeleteView, 
	UpdateView
)
from .models import ProjectModel

# Create your views here.
class ProjectKategoriListView(ListView):
	model = ProjectModel
	template_name = "project/project_kategori_list.html"
	context_object_name = 'project_list'
	ordering = ['-published']
	paginate_by = 5

	def get_queryset(self):
		self.queryset = self.model.objects.filter(kategori=self.kwargs['kategori'])
		return super().get_queryset()
	
	def get_context_data(self,*args,**kwargs):
		kategori_list = self.model.objects.values_list('kategori', flat=True).distinct().exclude(kategori=self.kwargs['kategori'])
		self.kwargs.update({'kategori_list':kategori_list})
		kwargs = self.kwargs
		return super().get_context_data(*args,**kwargs)

class ProjectListView(ListView):
	model = ProjectModel
	template_name = "project/project_list.html"
	context_object_name = 'project_list'
	ordering = ['-published']
	paginate_by = 5

	def get_context_data(self,*args,**kwargs):
		kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
		self.kwargs.update({'kategori_list':kategori_list})
		kwargs = self.kwargs
		return super().get_context_data(*args,**kwargs)

class ProjectDetailView(DetailView):
	model = ProjectModel
	template_name = "project/project_detail.html"
	context_object_name = 'project_detail'
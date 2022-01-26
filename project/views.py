from ast import arg
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import (
	ListView, 
	DetailView, 
)
from .models import ProjectModel
from django.db.models import Count

class ProjectPerKategori():
	model = ProjectModel

	def get_latest_project_each_kategori(self):
		kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
		QuerySet = []

		for kategori in kategori_list:
			project = self.model.objects.filter(kategori=kategori).latest('published')
			QuerySet.append(project)
		return QuerySet

class ProjectKategoriListView(ListView):
	model = ProjectModel
	template_name = "project/project_kategori_list.html"
	context_object_name = 'project_list'
	ordering = ['-published']
	paginate_by = 3

	def get_queryset(self):
		self.queryset = self.model.objects.filter(kategori=self.kwargs['kategori'])
		return super().get_queryset()
	
	def get_context_data(self,*args,**kwargs):
		kategori_count = self.model.objects.values('kategori').annotate(category_count=Count('kategori')).exclude(kategori=self.kwargs['kategori'])
		self.kwargs.update({'kategori_count':kategori_count})
		kwargs = self.kwargs
		return super().get_context_data(*args,**kwargs)

class ProjectListView(ListView):
	model = ProjectModel
	template_name = "project/project_list.html"
	context_object_name = 'project_list'
	ordering = ['-published']
	paginate_by = 3

	def get_queryset(self):
		query = self.request.GET.get('Searched')
		if query:
			object_list = self.model.objects.filter(judul__contains=query).order_by('-published')
		else:
			object_list = self.model.objects.all().order_by('-published')
		return object_list

	def get_context_data(self,*args,**kwargs):
		kategori_count = self.model.objects.values('kategori').annotate(category_count=Count('kategori'))
		self.kwargs.update({'kategori_count':kategori_count})
		
		kwargs = self.kwargs
		return super().get_context_data(*args,**kwargs)

class ProjectDetailView(DetailView):
	model = ProjectModel
	template_name = "project/project_detail.html"
	context_object_name = 'project_detail'

	def get_context_data(self, *args, **kwargs):
		kategori_count = self.model.objects.values('kategori').annotate(category_count=Count('kategori'))
		self.kwargs.update({'kategori_count':kategori_count})

		project_serupa = self.model.objects.filter(kategori=self.object.kategori).exclude(id=self.object.id)
		self.kwargs.update({'project_serupa':project_serupa})

		kwargs = self.kwargs
		return super().get_context_data(*args, **kwargs)
		
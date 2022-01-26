from pyexpat import model
from django.shortcuts import render
from django.views.generic import TemplateView
from project.views import ProjectPerKategori
from .models import projectDoneModel

class HomeView(TemplateView, ProjectPerKategori):
    template_name = "home/index.html"

    def get_context_data(self):
        queysets = self.get_latest_project_each_kategori()
        counries = projectDoneModel.objects.count()
        project_suc = projectDoneModel.objects.values('Counties').count()
        Happy_client = projectDoneModel.objects.values('Happy_client').count()
        print(Happy_client)

        context = {
            'latest_project_list' : queysets,
            'counries' : counries,
            'project_suc' : project_suc,
            'Happy_client': Happy_client
        }
        return context

class AboutView(TemplateView):
    template_name = "home/about/about.html"

class KostView(TemplateView):
    template_name = "home/kost/kost.html"
from django.shortcuts import render
from django.views.generic import TemplateView
from project.views import ProjectPerKategori

class HomeView(TemplateView, ProjectPerKategori):
    template_name = "home/index.html"

    def get_context_data(self):
        queysets = self.get_latest_project_each_kategori()
        context = {
            'latest_project_list' : queysets
        }
        return context

class AboutView(TemplateView):
    template_name = "home/about/about.html"

class KostView(TemplateView):
    template_name = "home/kost/kost.html"
from django.contrib import admin
from .models import ProjectModel
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=[
		'slug',
		'updated',
		'published',
	]
admin.site.register(ProjectModel, ProjectAdmin)
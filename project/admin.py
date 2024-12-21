from django.contrib import admin
from project.models import projectsdata

admin.site.site_header = "My Custom Admin Header"
admin.site.site_title = "My Custom Admin Title"
admin.site.index_title = "Welcome to My Custom Admin"

class projectAdmin(admin.ModelAdmin):
    list_display=('img','project','project_link','about')

admin.site.register(projectsdata,projectAdmin)
# Register your models here.

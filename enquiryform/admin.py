from django.contrib import admin
from enquiryform.models import enquiryform

admin.site.site_header = "My Custom Admin Header"
admin.site.site_title = "My Custom Admin Title"
admin.site.index_title = "Welcome to My Custom Admin"


class enquiryformAdmin(admin.ModelAdmin):
    list_display=('name','email','mobile','yenquiry')

admin.site.register(enquiryform,enquiryformAdmin)




# Register your models here.

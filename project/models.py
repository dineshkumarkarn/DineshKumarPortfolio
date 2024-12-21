from django.db import models

class projectsdata(models.Model):
    img=models.FileField(upload_to="projectimg/",max_length=250,null=True,default=None)
    project=models.CharField(max_length=500)
    project_link=models.CharField(max_length=500)
    about=models.TextField()

# Create your models here.

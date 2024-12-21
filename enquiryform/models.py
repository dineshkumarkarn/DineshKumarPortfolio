from django.db import models
class enquiryform(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    mobile=models.CharField(max_length=15)
    yenquiry=models.TextField()
# Create your models here.




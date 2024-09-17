from django.db import models
from django_ckeditor_5.fields import CKEditor5Field # type: ignore

class BreifServiceModels(models.Model):
    content = CKEditor5Field(config_name='extends')
    image = models.ImageField(upload_to='Services/', null=True, blank=True)
    topic = models.CharField(max_length=100)

class ServiceModels(models.Model):
    name = models.TextField(max_length=50)
    content = models.TextField(max_length=150)
    iconClass = models.TextField(max_length=100)
    briefModel = models.ForeignKey(BreifServiceModels, on_delete=models.CASCADE)

class TestimonialModels(models.Model):
    image = models.ImageField(upload_to='testimonial/',null=True, blank=True)
    name=models.CharField(max_length=50)
    text=models.TextField(max_length=200)
    position=models.CharField(max_length=100)

class ContactModels(models.Model):
    email=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    workingHrs=models.CharField(max_length=150)
    workingweekend=models.CharField(max_length=150)

class mentorsModels(models.Model):
    image = models.ImageField(upload_to='mentors/',null=True, blank=True)
    name=models.CharField(max_length=80)
    expertise=models.CharField(max_length=150)
    website=models.CharField(max_length=200)
    order=models.IntegerField(null=True,default="0")


class ScrollContenModel(models.Model):
    text1=models.CharField(max_length=100,blank=True,null=True)
    text2=models.CharField(max_length=100,blank=True,null=True)
    text3=models.CharField(max_length=100,blank=True,null=True)
    text4=models.CharField(max_length=100,blank=True,null=True)
    text5=models.CharField(max_length=100,blank=True,null=True)
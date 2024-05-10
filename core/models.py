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

class AboutCards(models.Model):
    iconClass=models.CharField(max_length=100)
    numbers=models.IntegerField()
    name=models.CharField(max_length=100)

class QuoteModels(models.Model):
    image = models.ImageField(upload_to='Quoters/',null=True, blank=True)
    h5tag = models.CharField(max_length=50)
    paragraph1 = CKEditor5Field(config_name='extends')
    regards = CKEditor5Field(config_name='extends')

class WorkModels(models.Model):
    image = models.ImageField(upload_to='works/',null=True, blank=True)
    prjName=models.CharField(max_length=100)
    desc=models.TextField(max_length=250)

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
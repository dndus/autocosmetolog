from django.db import models
from auto.minixs import TranslateMixin


class Carousel(TranslateMixin, models.Model):
    translate_attributes = ['title']


    PAGE_IMAGE_CHOICES = (
    ('INDEX', 'index'),
    ('SERVICE', 'service'),
    ('LOCATION', 'location'),
    ('ABOUT', 'about'),
    ('CAREER', 'career')
    )
    image = models.ImageField(upload_to='uploads/banner/')
    title_ru = models.CharField(max_length=100, null=True, default=None, blank=True,)
    title_uz = models.CharField(max_length=100, null=True, default=None, blank=True,)
    page = models.CharField(max_length=10, choices=PAGE_IMAGE_CHOICES, blank=True, null=True)
    

class Post(TranslateMixin, models.Model):
    translate_attributes = ['title']

    video = models.FileField(upload_to='uploads/videos/')
    title_ru = models.CharField(max_length=300, blank=True, null=True, default=None)
    title_uz = models.CharField(max_length=300, blank=True, null=True, default=None)
    views = models.IntegerField(default=0)


class AboutText(TranslateMixin, models.Model):
    translate_attributes = ['h3', 'text']

    entrance_ru = models.CharField(max_length=150, null=False, blank=False)
    entrance_uz = models.CharField(max_length=150, null=False, blank=False)
    entrantext_ru = models.TextField()
    entrantext_uz = models.TextField()
    h3_ru = models.CharField(max_length=100, null=False, blank=False)
    h3_uz = models.CharField(max_length=100, null=False, blank=False)
    text_ru = models.CharField(max_length=2000)
    text_uz = models.CharField(max_length=2000)


class EntranceAbout(TranslateMixin, models.Model):
    translate_attributes = ['entrance', 'entrantext']

    entrance_ru = models.CharField(max_length=150, null=False, blank=False)
    entrance_uz = models.CharField(max_length=150, null=False, blank=False)
    entrantext_ru = models.TextField()
    entrantext_uz = models.TextField()


class Testimonial(TranslateMixin, models.Model):
    translate_attributes = ['text']

    image = models.ImageField(upload_to='uploads/about')
    author = models.CharField(max_length=60)
    text_ru = models.TextField(blank=False, null=False)
    text_uz = models.TextField(blank=False, null=False)

class ServiceInfo(models.Model):
    PAGE_IMAGE_CHOICES = (
    ('Air', 'air'),
    ('Ceramic', 'ceramic'),
    ('Dry', 'dry'),
    )
    image = models.ImageField(upload_to='upload/service')
    work = models.CharField(max_length=10, choices=PAGE_IMAGE_CHOICES, blank=True, null=True)
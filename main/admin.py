from typing import List
from django.contrib import admin
from django.db.models import fields
from .models import Carousel, Post, AboutText, Testimonial, EntranceAbout, ServiceInfo


@admin.register(Carousel)
class AdminCarousel(admin.ModelAdmin):
    list_display = [
        'id',
        'image',
        'title_ru',
        'title_uz',
        'page'
    ]
    fields = ('image', 'title_ru', 'title_uz', 'page')


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = [
        'id',
        'video',
        'title_ru',
        'title_uz',
        'views'
    ]
    fields = ('video', 'title_ru', 'title_uz')


@admin.register(AboutText)
class AboutAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'h3_ru',
        'h3_uz',
        'text_ru',
        'text_uz'
    ]
    fields = ('h3_ru', 'h3_uz', 'text_ru', 'text_uz')


@admin.register(EntranceAbout)
class EntranceAbout(admin.ModelAdmin):
    list_display = [
        'entrance_ru',
        'entrance_ru',
        'entrantext_ru',
        'entrantext_uz',
    ]

    fields = ('entrance_ru', 'entrance_uz', 'entrantext_ru', 'entrantext_uz')

    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'text_ru',
        'text_uz'
    ]
    exculde = ('id')

@admin.register(ServiceInfo)
class ServiceInfoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'image',
        'work'
    ]
    exculde = ('id')
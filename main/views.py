from django.shortcuts import render
from .models import Carousel, EntranceAbout, Post, Testimonial, AboutText, ServiceInfo
from django.utils.translation import gettext as _

def main_index(request):
    sarlavha = _("Главный")
    return render(request, 'main/index.html', context={
        'carousel': Carousel.objects.all(),
        'owl': Testimonial.objects.all(),
        'page_title': sarlavha
    })


def main_service(request):
    sarlavha = _("Услуга")
    return render(request, 'main/service.html', context={
        'carousel': Carousel.objects.all(),
        'page_title': sarlavha
    })


def main_location(request):
    sarlavha = _("Локации")
    return render(request, 'main/location.html', context={
        'carousel': Carousel.objects.all(),
        'page_title': sarlavha
    })


def main_about(request):
    sarlavha = _("О нас")
    return render(request, 'main/about.html', context={
        'carousel': Carousel.objects.all(),
        'about': AboutText.objects.all(), 
        'entran': EntranceAbout.objects.all(),
        'page_title': sarlavha
    })


def main_career(request):
    sarlavha = _("Портфолио")
    return render(request, 'main/career.html', context={
        'carousel': Carousel.objects.all(),
        'page_title': sarlavha,
        'posts': Post.objects.all()
    })

def main_air(request):
    sarlavha = _("Кондиционер")
    return render(request, 'service/air.html', {
        'posts': ServiceInfo.objects.all(),
        'page_title': sarlavha
    })

def main_ceramic(request):
    sarlavha = _("Керамика")

    return render(request, 'service/ceramic.html', {
        'posts': ServiceInfo.objects.all(),
        'page_title': sarlavha
    })

def main_dry(request):
    sarlavha = _("Химчистка")

    return render(request, 'service/dry.html', {
        'posts': ServiceInfo.objects.all(),
        'page_title': sarlavha
    })
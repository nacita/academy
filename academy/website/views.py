from django.shortcuts import render

from academy.apps.accounts.models import Instructor


def index(request):
    context = {
        'title': 'Home',
        'instructors': Instructor.objects.order_by('order'),
    }
    return render(request, 'website/home.html', context)


def faq(request):
    context = {
        'title': 'Tilil (Q&A)'
    }
    return render(request, 'website/faq.html', context)


def home(request):
    context = {
        'title': 'Home 2'
    }
    return render(request, 'website/home2.html', context)


def error_404(request):
    return render(request, '404.html', {})


def error_500(request):
    return render(request, '500.html', {})
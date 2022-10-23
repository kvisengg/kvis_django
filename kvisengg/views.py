from django.shortcuts import render

from content.models import AboutUs


def index(request):
    about = AboutUs.objects.last()
    return render(request, 'base.html', {'about': about})

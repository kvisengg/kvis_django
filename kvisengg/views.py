from django.shortcuts import render

from content.models import AboutUs, Product, ProjectComplete, Reviews


def index(request):
    about = AboutUs.objects.last()
    project_complete = ProjectComplete.objects.last()
    products = Product.objects.all()
    reviews = Reviews.objects.all()
    payload = dict(
        about=about, project_complete=project_complete, products=products, reviews=reviews)
    return render(request, 'base.html', payload)

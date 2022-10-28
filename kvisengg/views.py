from django.shortcuts import render

from content.models import AboutUs, Portfolio, Product, ProjectComplete, Reviews, Team


def index(request):
    about = AboutUs.objects.last()
    project_complete = ProjectComplete.objects.last()
    products = Product.objects.all()
    reviews = Reviews.objects.all()
    teams = Team.objects.all()
    portfolio = Portfolio.objects.all()
    payload = dict(
        about=about, project_complete=project_complete, products=products, reviews=reviews, teams=teams, portfolio=portfolio)
    return render(request, 'base.html', payload)

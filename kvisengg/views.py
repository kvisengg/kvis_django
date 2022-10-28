from django.shortcuts import render
from content.forms import ContactForm

from content.models import AboutUs, Portfolio, Product, ProjectComplete, Reviews, Team


def index(request):
    about = AboutUs.objects.last()
    project_complete = ProjectComplete.objects.last()
    products = Product.objects.all()
    reviews = Reviews.objects.all()
    teams = Team.objects.all()
    portfolio = Portfolio.objects.all()
    payload = dict(
        about=about, project_complete=project_complete, products=products, reviews=reviews, teams=teams, portfolio=portfolio, contact_form=ContactForm()
    )
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            payload['success'] = True
            return render(request, 'base.html', payload)
    return render(request, 'base.html', payload)

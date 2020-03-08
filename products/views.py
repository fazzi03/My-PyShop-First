from  django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# when url request like /products it should call this index function below
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def new(request):
    return HttpResponse("New Products")

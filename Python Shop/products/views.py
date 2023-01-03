from django.http import HttpResponse
from django.shortcuts import render
from .models import Product #we are importing the product class
# Create your views here.


# /products -> index 
def index(request):
    products = Product.objects.all( )
    # return HttpResponse('Hello World')
    return render(request, 'index.html',{'products':products})


def new(request):
    return HttpResponse('New products page')
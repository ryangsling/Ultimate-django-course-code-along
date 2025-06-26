from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Product
from django.db.models import Q,F
# Create your views here.
def say_hello(request):
    queryset = Product.objects.filter(inventory=F('price'))
    return render(request, 'hello.html',{'name':'Alif', 'products': list(queryset)})
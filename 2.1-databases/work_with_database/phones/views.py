from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect("catalog")


def show_catalog(request):
    sort = request.GET.get("sort", "id")
    if sort == "min_price":
        sort = "price"
    elif sort == "max_price":
        sort = "-price"
    template = "catalog.html"
    phones = Phone.objects.all().order_by(sort)
    context = {"phones": phones}
    return render(request, template, context)


def show_product(request, slug):
    template = "product.html"
    phone = Phone.objects.get(slug__exact=slug)
    context = {"phone": phone}
    return render(request, template, context)

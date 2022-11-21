from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm


def create_product(request):
    form = ProductForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            img = request.FILES['image']
            location = "upload/" + img.name
            post = form.save(commit=False)
            post.author = request.user
            post.image = location
            post.save()
            handle_uploaded_file(img)
    context = {
        "form": form
    }
    return render(request, 'createform.html', context)


def view_product(request):
    # Retrieve data from db
    queryset = Product.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, 'viewproducts.html', context)


def handle_uploaded_file(f):
    with open('testdb/static/upload/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

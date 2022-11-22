from django.shortcuts import get_object_or_404, render, redirect
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
        else:
            form = ProductForm()
    context = {
        "form": form
    }
    return render(request, 'createproduct.html', context)


def view_product(request):
    # Retrieve data from db
    queryset = Product.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, 'viewproducts.html', context)


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        product.delete()
        return redirect('/products/')

    queryset = Product.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, 'viewproducts.html', context)


def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST, instance=product)
    if request.method == "POST":
        if form.is_valid():
            img = request.FILES['image']
            location = "upload/" + img.name
            post = form.save(commit=False)
            post.image = location
            post.save()
            handle_uploaded_file(img)
            return redirect('/products/', pk=id)
        else:
            form = ProductForm(instance=product)
    context = {
        "form": form
    }
    return render(request, 'editproduct.html', context)


def handle_uploaded_file(f):
    with open('testdb/static/upload/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

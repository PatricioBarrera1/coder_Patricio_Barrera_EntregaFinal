from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProductForm
from .models import Product

def list_products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'app_productos/product_list.html', context)

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_productos:list_products')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'app_productos/product_create.html', context)

def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('app_productos:list_products')
    else:
        form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, 'app_productos/product_update.html', context)

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('app_productos:list_products')
    context = {'product': product}
    return render(request, 'app_productos/product_delete.html', context)
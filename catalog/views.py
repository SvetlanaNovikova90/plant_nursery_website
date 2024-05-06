from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    return render(request, "catalog/index.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
    return render(request, "catalog/contact.html")


def products(request):
    product = Product.objects.all()
    context = {'object_list': product}
    return render(request, "catalog/products.html", context)

def products_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, "catalog/product_detail.html", context)



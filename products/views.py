from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.urls import reverse
from django.db.models import Max, Min
from .models import *
from .forms import ProductForm, CommentForm
from cart.forms import CartAddProductForm


# Create your views here.

def sell(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        print(ProductForm.errors)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect(reverse('sell'))
        else:
            return HttpResponse("Form Failed to Validate")

    else:
        form = ProductForm()
        return render(request, 'product.html', {'form': form})


'''
def listing(request, type_slug=None):
    type = None
    types = Type.objects.all()
    color = Product.objects.order_by().values_list('color').distinct()
    products = Product.objects.filter(available=True, status='Active')
    count = products.count()
    colcount = color.count()
    price_max = Product.objects.filter(system=type).aggregate(Max('total'))
    price_min = Product.objects.filter(system=type).aggregate(Min('total'))
    mint = Product.objects.filter(condition='Mint').count()
    good = Product.objects.filter(condition='Good').count()
    fair = Product.objects.filter(condition='Fair').count()
    new = Product.objects.filter(condition='New').count()

    if type_slug:
        type = get_object_or_404(Type, slug=type_slug)
        products = products.filter(system=type)
        # return HttpResponseRedirect('listing')
    return render(request, 'listing.html',
                  {'type': type, 'types': types, 'products': products, 'count': count, 'new': new, 'mint': mint,
                   'good': good, 'fair': fair, 'color': color, 'colcount': colcount, 'price_min': price_min,
                   'price_max': price_max})


'''


def product_list(request, type_slug=None):
    type = None
    types = Type.objects.filter(device='1')

    if type_slug:
        type = get_object_or_404(Type, slug=type_slug)
    return render(request, 'iphone.html', {'type': type, 'types': types})


def list(request, type_slug=None):
    products = Product.objects.filter(available=True, status='Active')
    mint = Product.objects.filter(condition='Mint').count()
    good = Product.objects.filter(condition='Good').count()
    fair = Product.objects.filter(condition='Fair').count()
    new = Product.objects.filter(condition='New').count()

    if type_slug:
        type = get_object_or_404(Type, slug=type_slug)
        products = products.filter(system=type)
        color = products.order_by().values_list('color__name').distinct()
        colcount = color.count()
        count = products.count()
        price_max = Product.objects.filter(system=type).aggregate(Max('total'))
        price_min = Product.objects.filter(system=type).aggregate(Min('total'))
    return render(request, 'listing.html',
                  {'type': type, 'products': products, 'count': count, 'new': new, 'mint': mint,
                   'good': good, 'fair': fair, 'color': color, 'colcount': colcount, 'price_min': price_min,
                   'price_max': price_max})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True, status='Active')
    products = Product.objects.filter(available=True, status='Active')
    images = Images.objects.all()
    comments = Comment.objects.all()
    com = comments.count()
    sold = Product.objects.filter(available=False)
    count = products.count()
    socount = sold.count()

    cart_product_form = CartAddProductForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        print(CommentForm.errors)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()

    else:
        form = CommentForm()
    return render(request, 'detail.html',
                  {'form': form, 'count': count, 'product': product, 'products': products, 'sold': sold,
                   'socount': socount, 'image': images, 'comments': comments, 'com': com,
                   'cart_product_form': cart_product_form})

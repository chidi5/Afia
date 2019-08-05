from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import EditProfileForm
from products.models import Product


# Create your views here.

@login_required
def me(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, files=request.FILES, instance=request.user)
        print(EditProfileForm.errors)
        if form.is_valid():
            # user = form.save(commit=False)
            # user.name = request.user
            form.save()
            return redirect(reverse('me'))
        else:
            return HttpResponse("Form Failed to Validate")

    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'me.html', {'form': form})


@login_required
def profile(request):
    products = Product.objects.filter(available=True, status='Active', user=request.user)
    count = products.count()

    context = {
        'count': count,
        'products': products,
    }
    return render(request, 'profile.html', context)

from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_objects = Phone.objects.all()
    phones = [{'name': p.name, 'slug': p.slug, 'image': p.image, 'price': p.price} for p in phones_objects]
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)

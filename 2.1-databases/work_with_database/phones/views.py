from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    template = 'catalog.html'
    if sort == "name":
        phones = Phone.objects.order_by('name').values('name', 'slug', 'image', 'price')
    elif sort == "min_price":
        phones = Phone.objects.order_by('price').values('name', 'slug', 'image', 'price')
    elif sort == "max_price":
        phones = Phone.objects.order_by('-price').values('name', 'slug', 'image', 'price')
    else:
        phones = Phone.objects.values('name', 'slug', 'image', 'price')
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.get(slug=slug)
    phone_item = {
        'name': phone_object.name,
        'slug': phone_object.slug,
        'image': phone_object.image,
        'price': phone_object.price,
        'release_date': phone_object.release_date,
        'lte_exists': phone_object.lte_exists,
    }
    context = {'phone': phone_item}
    return render(request, template, context)

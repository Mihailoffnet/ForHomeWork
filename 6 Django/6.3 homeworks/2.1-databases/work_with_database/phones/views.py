from django.shortcuts import render, redirect
from phones.models import Phone
from django.http import HttpResponse

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    # slug = request.GET.get('slug', '')
    print(f'url {slug=}')
    phone = Phone.objects.filter(slug=slug)
    for row in phone:
        name = row.name
        image = row.image
        price = row.price
        release_date = row.release_date
        lte_exists = row.lte_exist

    context = {
        'phone': phone,
        'name': name,
        'phone.image': image,
        'price': price,
        'release_date': release_date,
        'lte_exists': lte_exists,
        'image': image,

    }
    return render(request, template, context)

def create_phone(request):
    name = request.GET.get('name', 'noname')
    image = request.GET.get('image', None)
    price = request.GET.get('price', None)
    release_date = request.GET.get('release_date', None)
    lte = request.GET.get('lte', False)

    name = request.GET.get('name', name)
    image = request.GET.get('image', image)
    price = request.GET.get('price', price)
    release_date = request.GET.get('release_date', release_date)
    lte_exist = request.GET.get('lte_exist', lte)
    slug = name.replace(" ", "-")
    phone = Phone(name=name, image=image, price=price,
                  release_date=release_date, lte_exist=lte_exist, slug=slug)
    phone.save()
    print(f'В базу добавлен телефон: {id=}, {name=}, {price=}')
    return HttpResponse(f'В базу добавлен телефон: {name=}, {price=}')


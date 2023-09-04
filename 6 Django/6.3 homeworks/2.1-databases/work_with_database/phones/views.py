from django.shortcuts import render, redirect
from phones.models import Phone
from django.http import HttpResponse

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)

def create_phone(request):
    name = request.GET.get('name', '')
    image = request.GET.get('image', '')
    price = request.GET.get('price', '')
    release_date = request.GET.get('release_date', '')
    lte = request.GET.get('lte', '')

    name = request.GET.get('name', name)
    image = request.GET.get('image', image)
    price = request.GET.get('price', price)
    release_date = request.GET.get('release_date', release_date)
    lte_exist = request.GET.get('lte_exist', lte)
    slug = name.replace(" ", "-")
    phone = Phone(name=name, image=image, price=price,
                  release_date=release_date, lte_exist=lte_exist, slug=slug)
    phone.save()
    print(f'В базу добавлен телефон: {name=}, {price=}')
    return HttpResponse(f'В базу добавлен телефон: {name=}, {price=}')


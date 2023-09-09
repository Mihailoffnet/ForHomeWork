from django.shortcuts import render, redirect
from phones.models import Phone
from django.http import HttpResponse

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', '')

    if sort == 'name':
            phones = Phone.objects.order_by('name')
    elif sort == 'min_price':
            phones = Phone.objects.order_by('price')
    elif sort == 'max_price':
            phones = Phone.objects.order_by('price').reverse()
    else:
        phones = Phone.objects.all()
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)[0]
    print(phone.lte_exist)
    print(type(phone.lte_exist))
    context = {
        'phone': phone,
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


import csv

from django.core.management.base import BaseCommand
from django.http import HttpResponse
from phones.models import Phone
from pprint import pprint


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for row in phones:
                id = row.get('id')
                print(id)
                name = row.get('name', 'noname')
                image = row.get('image', None)
                price = row.get('price', None)
                release_date = row.get('release_date', None)
                if row.get('lte_exists') == 'True':
                    lte_exists = True
                else:
                    lte_exists = False
                slug = name.replace(" ", "-")

                phone = Phone(id=id, name=name, image=image, price=price,
                                     release_date=release_date,
                                     lte_exists=lte_exists, slug=slug)
                phone.save()
                print(f'В базу добавлен телефон {phone.name} и доступен по адресу http://127.0.0.1:8000/catalog/{slug}/')

            # return



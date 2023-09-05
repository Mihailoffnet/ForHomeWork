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
            msg = ''
            for row in phones:
                # phone_id = row.get('phone_id')
                name = row.get('name', 'noname')
                image = row.get('image', None)
                price = row.get('price', None)
                release_date = row.get('release_date', None)
                if row.get('lte_exists') == 'True':
                    lte_exist = True
                else:
                    lte_exist = False
                slug = name.replace(" ", "-")

                phone = Phone(name=name, image=image, price=price,
                                     release_date=release_date,
                                     lte_exist=lte_exist, slug=slug)
                phone.save()
                print(f'В базу добавлен телефон {phone.name} и доступен по адресу http://127.0.0.1:8000/catalog/{slug}/')

            # return



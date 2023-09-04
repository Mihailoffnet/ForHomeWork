from django.test import TestCase
from pprint import pprint
import csv
# Create your tests here.

def add_arguments(self, parser):
    pass

def handle(self, *args, **options):
    with open('phones.csv', 'r') as file:
        phones = list(csv.DictReader(file, delimiter=';'))
        for row in phones:
            name = row .get('name', '')
            image = row .get('image', '')
            price = row .get('price', '')
            release_date = row .get('release_date', '')
            lte_exist = row .get('lte_exist', False)
            slug = name.replace(" ", "-")
            print(name, image, price, release_date, lte_exist, slug)

    return phones

a = handle('')


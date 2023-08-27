from django.test import TestCase

# Create your tests here.
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

dishes = input('Введите блюдо: ')
quantity = int(input('Введите количество персон: '))

result_dict = {}
for key, value in DATA[dishes].items():
    print(key, value)
    result_dict[key] = round(value * int(quantity), 2)

print(result_dict)




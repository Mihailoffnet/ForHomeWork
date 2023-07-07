from pprint import pprint
import csv
import re

# Читаем адресную книгу в формате CSV в список contacts_list:
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# D справочнике CSV из задачи найдена строка
# c 8 столбцами вместо семи (лишняя запятая в конце)
# поэтому проверяем длину справоника и корректируем ее
count = -1
for row in contacts_list:
    count += 1
    while len(row) != 7:
        if len(row) > 7:
            row.pop(7)
        if len(row) < 7:
            row.append('')
    contacts_list[count] = row

# Разбиваем ФИО по полям
count = -1
for row in contacts_list:
    count += 1
    if ' ' in row[0]:
        temp_list = row[0].split()
        contacts_list[count][0] = temp_list[0]
        contacts_list[count][1] = temp_list[1]
        if len(temp_list) == 3:
            contacts_list[count][2] = temp_list[2]
count = -1
for row in contacts_list:
    count += 1
    if ' ' in row[1]:
        temp_list = row[1].split()
        contacts_list[count][1] = temp_list[0]
        contacts_list[count][2] = temp_list[1]

# Объединяем дубликаты записей 
new_contacts_list = contacts_list
count_row = -1
for row in contacts_list:
    count_row += 1
    count_new_row = -1
    for new_row in new_contacts_list:
        count_new_row += 1
        if row != new_row and row[0] == new_row[0] and row[1] == new_row[1]:
            count_item = -1
            for item in new_row:
                count_item += 1
                if item == '':
                    new_contacts_list[count_new_row][count_item]=contacts_list[
                        count_row][count_item]

# удаляем дубликаты:
final_contacts_list = []
[final_contacts_list.append(x) for x in new_contacts_list 
if x not in final_contacts_list]

print('Оптимизированный справочник:')
pprint(final_contacts_list)
print()

# форматируем номера телефонов

count_row = -1
for row in final_contacts_list:
    count_row += 1
    # паттерн получился более 79 символов. Разбил его на два и склеил, 
    # чтобы уложиться в PEP8. Или как лучше такое делать?
    pattern_1 = r"(\+7|8)\s*[\-\(]*(\d{3})[\s\-\)]*(\d{3})*[\s\-]*(\d{2})*"
    pattern_2 = r"[\s\-]*(\d{2})\s*\(*(доб.)*\s*(\d+)*\)*"
    pattern = f'{pattern_1}{pattern_2}'
    pattern_repl = r"+7(\2)\3-\4-\5 \6\7"
    phone = re.sub(pattern, pattern_repl, row[5])
    final_contacts_list[count_row][5] = phone

# 2. Сохраняем получившиеся данные в другой файл.

file_name = "phonebook.csv"
with open(file_name, "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',',    lineterminator='\n' )
    datawriter.writerows(final_contacts_list)
    print(f'Данные успешно помещены в файл {file_name}')


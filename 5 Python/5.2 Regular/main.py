from pprint import pprint
import csv
import re

# Читаем адресную книгу в формате CSV в список contacts_list:
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# 1. Выполните пункты 1-3 задания.

# Разбиваем ФИО по полям
count = -1
for row in contacts_list:
  count += 1
  # print(row[0])
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

print(final_contacts_list)

# форматируем номера телефонов

count_row = -1
for row in final_contacts_list:
  count_row += 1
  print(row[5])
  # pattern = r"(\+7|8)\s*[\-\(]*(\d+)[\s\-\)]*(\d+)*[\s\-]*(\d+)*[\s\-]*(\d+)*"
  pattern = r"\d*"
  pattern_repl = r"+7(\2)\3-\4-\5"
  phone = re.sub(pattern, pattern_repl, row[5])
  # phone2 = re.sub(r"доб.\s*(\d+)", r"доб.\1", row[5])
  final_contacts_list[count_row][5] = phone
  print(final_contacts_list[count_row][5])



# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',',  lineterminator='\n' )
  datawriter.writerows(final_contacts_list)


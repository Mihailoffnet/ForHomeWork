
import datetime 
from emoji import emojize 
# шпаргалка moji https://www.webfx.com/tools/emoji-cheat-sheet/
from application.salary import calculate_salary
from application.db.people import get_employees

date_now = datetime.datetime.now()
print(date_now.strftime('%m.%d.%Y'))

if __name__ == '__main__':

    calculate_salary(1, 2)
    get_employees('Viktor', 'Mikhaylov')
    # print(emojize(":robot:"))
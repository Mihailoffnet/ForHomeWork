import bs4
import fake_headers
import requests
import re
import json

headers = fake_headers.Headers(browser="firefox", os="win")
headers_dict = headers.generate()

link = 'https://hh.ru/search/vacancy'
search_text = 'description%3A%28python+AND+Flask+AND+Django%29'
s_params_1, s_params_2 = 'area=1', 'area=2'
search_period = 0 # поиск ваканский за последние Х дней (0 без ограничения)
sort = 'publication_time' # сортировка
page = 0
target_link = f'{link}?{s_params_1}&{s_params_2 }&ored_clusters=true&text={search_text}&order_by={sort}&items_on_page=20'
usd = False
file_name = "vacancy.json"
parsed_data = []
parsed_data_new = []

with open(file_name, "r", encoding="utf-8") as f:
    parsed_data = json.loads(f.read())

# print(txt[3])


def get_vacancies(url):
    response = requests.get(url, headers=headers_dict)
    main_html_data = response.text
    main_html = bs4.BeautifulSoup(main_html_data, "lxml")
    vacancies = main_html.find_all("div", class_="vacancy-serp-item__layout")
    return vacancies

if __name__ == '__main__':

    vacancies = get_vacancies(target_link)

    while len(vacancies) != 0:

        for item in vacancies:
            vacancy_url = item.find("a")['href']
            if item.find('span', class_='bloko-header-section-3'):
                salary = item.find('span', 
                                class_='bloko-header-section-3').get_text()
            else: 
                salary = "Зарплата не указана"

            company_name = list(item.find(
                class_='vacancy-serp-item__info').children)[0].text

            vacancy_name = item.find("a").get_text()

            city_raw = list(item.find(
                class_='vacancy-serp-item__info').children)[1].text
            city = re.sub(r"([a-яА-Я-]+)(\s|\.|\,)*(.)*", r"\1", city_raw)
            # print(vacancy_name)
            # print(company_name)
            # print(salary)
            # print(vacancy_url)
            # print(city)
            # print()
            temp_dict = {
                    "company_name": company_name,
                    "vacancy_name": vacancy_name,
                    "salary": salary,
                    "vacancy_url": vacancy_url,
                    "city": city,
                }
            
            if temp_dict in parsed_data:
              print(f'вакансия {vacancy_name} уже существует')
            else:
              print(f'Добавлена вакансия {vacancy_name}')
            parsed_data_new.append(
                {
                    "company_name": company_name,
                    "vacancy_name": vacancy_name,
                    "salary": salary,
                    "vacancy_url": vacancy_url,
                    "city": city,
                }
            )
        
        page += 1
        vacancies = get_vacancies(f'{target_link}&page={page}')

    print('Поиск вакансий завершен')
    print(f'Всего сохранено {len(parsed_data_new)} вакансий')

    with open(file_name, "w", encoding="utf-8") as f:
        f.write(json.dumps(parsed_data_new))
        print(f'Данные успешно помещены в файл {file_name}')

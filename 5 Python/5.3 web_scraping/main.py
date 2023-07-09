"""
https://hh.ru/search/vacancy?area=1&area=2&search_field=name&search_field=company_name&search_field=description&enable_snippets=false&text=description%3A%28python+AND+Flask+AND+Django%29
"""
# Маска очистки вакансии
"""
r"(.+)*\n*(.+)>(.+)</a>"
r"\3"
"""

# Маска очистки зарплаты
"""
r"(.+)compensation\">(.+)(₽|$|€)+</span>(.+)"
r"\2\3"
"""
"""
Описание вакансии:
<div class="vacancy-branded-user-content" itemprop="description" data-qa="vacancy-description"><p></div>
"""

import bs4
import fake_headers
import requests
import re


headers = fake_headers.Headers(browser="firefox", os="win")
headers_dict = headers.generate()

link = 'https://hh.ru/search/vacancy'
search_text = 'python'
s_params_1, s_params_2 = 'area=1', 'area=2'
search_period = 0 # поиск ваканский за последние Х дней (0 без ограничения)
sort = 'publication_time' # сортировка
page = 1
target_link = f'{link}?text={search_text}&{s_params_1}&{s_params_2 }&page={page}&order_by={sort}&search_period={search_period}'
usd = False
print(target_link)
print()

response = requests.get(url=target_link, headers=headers_dict)
main_html_data = response.text
main_html = bs4.BeautifulSoup(main_html_data, "lxml")


jobs_list = main_html.find("div", id="a11y-main-content")
vacancies = main_html.find_all("div", class_="vacancy-serp-item__layout")

parsed_data = []

for item in vacancies:
    vacancy_url = item.find("a")['href']
    salary_raw = item.find_all("span")
    if 'vacancy-serp__vacancy-compensation' in str(salary_raw):
        print()
        print('вхождение')
        print()
        salary = re.sub(r"(.+)compensation\">(.+)(₽|$|€)+</span>(.+)", r"\3\4", str(salary_raw))
    else: salary = None
    company_name_raw = item.find("a")
    company_name = re.sub(r"(.)*>(.+)</a>", r"\2", str(company_name_raw))
    print(company_name)
    print()
    print(salary)
    print()
    print(vacancy_url)
    print()
    print()
    # city_name = ''



    # a_tag = h2_tag.find("a")
    # span_tag = a_tag.find("span")
    # time_tag = article_tag.find("time")

#     link = f"https://habr.com{a_tag['href']}"
#     title = span_tag.text
#     date_time = time_tag["datetime"]

#     response = requests.get(link, headers=headers.generate()).text
#     article_html = bs4.BeautifulSoup(response, "lxml")
#     article_full_tag = article_html.find("div", id="post-content-body")
#     article_full_text = article_full_tag.text[100]

#     parsed_data.append(
#         {
#             "title": title,
#             "link": link,
#             "date_time": date_time,
#             "text": article_full_text,
#         }
#     )

# print(parsed_data)

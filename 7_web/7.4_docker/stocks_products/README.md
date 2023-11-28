* Соберите образ из заранее подготовленных файлов 
docker build . --tag=my_django_v1
* Запустите образ под именем v1 
docker run -d -p 8888:8000 --name=v1 my_django_v1
* Для проверки тестовой функции можно отправить запрос
curl localhost:8888/test/

* Другие запросы можно отправлять из файла через VS Code REST Client из файла requests-examples.http
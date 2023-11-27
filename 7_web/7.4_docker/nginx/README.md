* Скачайте docker образ nginx
```docker pull nginx```
* Соберите образ из заранее подготовленных файлов 
```docker build -t nginx_v1 .```
* Запустите образ под именем my_nginx1 
```docker run --name my_nginx1 -d -p 80:80 nginx_v1```
* Проверьте подмененную стартовую страницу сервиса
```curl localhost:80/```
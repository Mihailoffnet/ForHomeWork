docker build . --tag=my_django_v1
docker run -d -p 8090:8080 --name=v1 my_django_v1
curl localhost:8090/api/v1/test
import requests

response = requests.get(
    "http://127.0.0.1:5000/advert/1",
)
print(response.status_code)
print(response.text)

response = requests.post(
    "http://127.0.0.1:5000/advert",
    json={"title": "Python  String title() Method", "author_id": "1", "text": "PEP 8, sometimes spelled PEP8 or PEP-8, is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.This tutorial outlines the key guidelines laid out in PEP 8. It’s aimed at beginner to intermediate programmers, and as such I have not covered some of the most advanced topics. You can learn about these by reading the full  PEP 8 documentation."},
)
print(response.status_code)
print(response.text)

response = requests.get(
    "http://127.0.0.1:5000/advert/1",
)
print(response.status_code)
print(response.text)

response = requests.patch("http://127.0.0.1:5000/advert/1", json={"title": "3 How to Write Beautiful Python Code With PEP 8"},)
print(response.status_code)
print(response.text)

response = requests.get(
    "http://127.0.0.1:5000/advert/1",
)
print(response.status_code)
print(response.text)

response = requests.delete(
    "http://127.0.0.1:5000/advert/1",
)
print(response.status_code)
print(response.text)

response = requests.get(
    "http://127.0.0.1:5000/advert/1",
)
print(response.status_code)
print(response.text)
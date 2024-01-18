import asyncio

import aiohttp


async def main():
    client = aiohttp.ClientSession()


    response = await client.get(
        "http://127.0.0.1:8080/advert/1",
        )
    print(response.status)
    print(await response.json())


    response = await client.post(
        'http://127.0.0.1:8080/advert',
        json={"author_id": 1, "title": "Python  String title() Method", "text": "PEP 8...."},
        )
    print(response.status)
    print(await response.json())

    
    response = await client.get(
        "http://127.0.0.1:8080/advert/1",
        )
    print(response.status)
    print(await response.json())

    response = await client.post(
        "http://127.0.0.1:8080/advert",
        json={"title": "test_2", "text": "test test test"},
        )
    print(response.status)
    print(await response.json())
    

    response = await client.get(
        "http://127.0.0.1:8080/advert/1",
        )
    print(response.status)
    print(await response.json())


    response = await client.patch(
        "http://127.0.0.1:8080/advert/1",
        json={"title": "3 How to Write Beautiful Python Code With PEP 8"},
        )
    print(response.status)
    print(await response.json())


    response = await client.get(
        "http://127.0.0.1:8080/advert/1",
        )
    print(response.status)
    print(await response.json())
    

    response = await client.delete(
        "http://127.0.0.1:8080/advert/1",
        )
    print(response.status)
    print(await response.json())


    response = await client.get(
        "http://127.0.0.1:8080/advert/1",
        )
    print(response.status)
    print(await response.json())


    await client.close()


asyncio.run(main())

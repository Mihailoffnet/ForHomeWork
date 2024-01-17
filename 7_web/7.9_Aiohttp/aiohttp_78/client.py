import asyncio

import aiohttp


async def main():
    client = aiohttp.ClientSession()

    response = await client.post(
        'http://127.0.0.1:8080/hello/world',
        json={'name': 'user_1', 'password': '123456'},
        params={'name': 'Viktor', 'surname': 'Mihailoff'}, # query strings
        headers={'token': 'secret'},

    )
    print(response.status)
    print(await response.json())

    await client.close()

    # response = await client.get(
    #     "http://127.0.0.1:8080/user/10000",
    # )
    # print(response.status)
    # print(await response.json())

    # response = await client.patch(
    #     "http://127.0.0.1:8080/user/1",
    #     json={"name": "new_user",},
    # )
    # print(response.status)
    # print(await response.json())

    # response = await client.get(
    #     "http://127.0.0.1:8080/user/1",
    # )
    # print(response.status)
    # print(await response.json())
    #
    # await client.close()

    # response = await client.delete(
    #     "http://127.0.0.1:8080/user/4",
    # )
    # print(response.status)
    # print(await response.json())

    # response = await client.get(
    #     "http://127.0.0.1:8080/user/4",
    # )
    # print(response.status)
    # print(await response.json())
    # #
    # await client.close()


asyncio.run(main())

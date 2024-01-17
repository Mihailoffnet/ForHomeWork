import asyncio
import datetime
import requests

import aiohttp
from more_itertools import chunked

from models import Session, SwapiPeople, close_db, init_db
from pprint import pprint

CHUNK_SIZE = 10


async def insert_people(people_list):
    people_list = [SwapiPeople(json=person) for person in people_list]
    async with Session() as session:
        session.add_all(people_list)

        await session.commit()

def get_len():
    json_response = requests.get(f"https://swapi.py4e.com/api/people/").json()
    print(json_response["count"])
    len = json_response["count"]

    return len

async def get_person(person_id):
    session = aiohttp.ClientSession()
    response = await session.get(f"https://swapi.py4e.com/api/people/{person_id}/")
    json_response = await response.json()
    print(len(json_response))
    if len(json_response) > 1:
        for film in json_response['films']:
            print(film)
    else: 
        json_response = {"error": "object not found"}
    await session.close()
    return json_response
    

async def main():

    range_len = get_len() + 1

    await init_db()
    for person_id_chunk in chunked(range(1, range_len), CHUNK_SIZE):
        coros = [get_person(person_id) for person_id in person_id_chunk]
        result = await asyncio.gather(*coros)
        print(f'запись пачки {person_id_chunk}')
        print(f'пачка {result}')
        asyncio.create_task(insert_people(people_list=result))
    tasks = asyncio.all_tasks() - {asyncio.current_task()}
    await asyncio.gather(*tasks)
    await close_db()


if __name__ == "__main__":
    start = datetime.datetime.now()
    asyncio.run(main())
    print(datetime.datetime.now() - start)

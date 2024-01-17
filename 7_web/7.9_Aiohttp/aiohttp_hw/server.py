import json

# import bcrypt
from aiohttp import web
from sqlalchemy.exc import IntegrityError

from models import Session, Advert, engine, init_db
# from schema import CreateAdvert, UpdateAdvert


# def hash_password(password: str):
#     password = password.encode()
#     password = bcrypt.hashpw(password, bcrypt.gensalt())
#     password = password.decode()
#     return password


# def check_password(password: str, hashed_password: str):
#     password = password.encode()
#     hashed_password = hashed_password.encode()
#     return bcrypt.checkpw(password, hashed_password)


app = web.Application()


@web.middleware
async def session_middleware(request: web.Request, handler):
    async with Session() as session:
        request.session = session
        response = await handler(request)
        return response


async def init_orm(app: web.Application):
    print("START")
    await init_db()
    yield
    await engine.dispose()
    print("FINISH")


app.cleanup_ctx.append(init_orm)
app.middlewares.append(session_middleware)


def get_http_error(error_class, message):
    error = error_class(
        body=json.dumps({"error": message}), content_type="application/json"
    )
    return error


async def get_advert_by_id(session: Session, advert_id: int):
    advert = await session.get(Advert, advert_id)
    if advert is None:
        raise get_http_error(
            web.HTTPNotFound, f"Advert with id {advert_id} not found"
            )
    return advert


async def add_advert(session: Session, advert: Advert):
    try:
        session.add(advert)
        await session.commit()
    except IntegrityError as error:
        raise get_http_error(web.HTTPConflict, "Advert already exists")
    return advert


class AdvertView(web.View):
    @property
    def advert_id(self):
        return int(self.request.match_info["advert_id"])

    @property
    def session(self) -> Session:
        return self.request.session

    async def get_current_advert(self):
        return await get_advert_by_id(self.session, self.advert_id)

    async def get(self):
        advert = await self.get_current_advert()
        return web.json_response(advert.dict)

    async def post(self):
        json_data = await self.request.json()
        # json_data = await validate(CreateAdvert, self.request.json())
        # json_data["password"] = hash_password(json_data["password"])
        advert = Advert(**json_data)
        advert = await add_advert(self.session, advert)
        return web.json_response({"id": advert.id})

    async def patch(self):
        json_data = await self.request.json()
        # json_data = await validate(UpdateAdvert, self.request.json())
        advert = await self.get_current_advert()
        # if "password" in json_data:
        #     json_data["password"] = hash_password(json_data["password"])
        for field, value in json_data.items():
            setattr(advert, field, value)
        advert = await add_advert(self.session, advert)
        return web.json_response(advert.dict)

    async def delete(self):
        advert = await self.get_current_advert()
        await self.session.delete(advert)
        await self.session.commit()
        return web.json_response({"status": "deleted"})


app.add_routes(
    [
        web.post("/advert", AdvertView),
        web.get("/advert/{advert_id:\d+}", AdvertView),
        web.patch("/advert/{advert_id:\d+}", AdvertView),
        web.delete("/advert/{advert_id:\d+}", AdvertView),
    ]
)
web.run_app(app)

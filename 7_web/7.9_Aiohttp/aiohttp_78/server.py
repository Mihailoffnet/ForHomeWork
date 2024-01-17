import json

import bcrypt
from aiohttp import web
from sqlalchemy.exc import IntegrityError

from models import Session, User, engine, init_db

async def hello_world(request):
    json_data = await request.json() # ожидаем передачу json
    headers = request.headers # ожидаем передачу заголовков
    params = request.query # ожидаем передачу query string параметров
    
    print(f'{json_data=}')
    print(f'{headers=}')
    print(f'{params=}')
    
    return web.json_response({'hello': 'world'})


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

app.add_routes(
    [
        web.post("/hello/world", hello_world),
    ]
)

# @web.middleware
# async def session_middleware(request: web.Request, handler):
#     async with Session() as session:
#         request.session = session
#         response = await handler(request)
#         return response


async def init_orm(app: web.Application):
    print("START")
    await init_db()
    yield
    await engine.dispose()
    print("FINISH")


app.cleanup_ctx.append(init_orm)
# app.middlewares.append(session_middleware)


# def get_http_error(error_class, message):
#     error = error_class(
#         body=json.dumps({"error": message}), content_type="application/json"
#     )
#     return error


# async def get_user_by_id(session: Session, user_id: int):
#     user = await session.get(User, user_id)
#     if user is None:
#         raise get_http_error(web.HTTPNotFound, f"User with id {user_id} not found")
#     return user


# async def add_user(session: Session, user: User):
#     try:
#         session.add(user)
#         await session.commit()
#     except IntegrityError as error:
#         raise get_http_error(web.HTTPConflict, "User already exists")
#     return user


# class UserView(web.View):
#     @property
#     def user_id(self):
#         return int(self.request.match_info["user_id"])

#     @property
#     def session(self) -> Session:
#         return self.request.session

#     async def get_current_user(self):
#         return await get_user_by_id(self.session, self.user_id)

#     async def get(self):
#         user = await self.get_current_user()
#         return web.json_response(user.dict)

#     async def post(self):
#         json_data = await self.request.json()
#         json_data["password"] = hash_password(json_data["password"])
#         user = User(**json_data)
#         user = await add_user(self.session, user)
#         return web.json_response({"id": user.id})

#     async def patch(self):
#         json_data = await self.request.json()
#         user = await self.get_current_user()
#         if "password" in json_data:
#             json_data["password"] = hash_password(json_data["password"])
#         for field, value in json_data.items():
#             setattr(user, field, value)
#         user = await add_user(self.session, user)
#         return web.json_response(user.dict)

#     async def delete(self):
#         user = await self.get_current_user()
#         await self.session.delete(user)
#         await self.session.commit()
#         return web.json_response({"status": "deleted"})


# app.add_routes(
#     [
#         web.post("/user", UserView),
#         web.get("/user/{user_id:\d+}", UserView),
#         web.patch("/user/{user_id:\d+}", UserView),
#         web.delete("/user/{user_id:\d+}", UserView),
#     ]
# )
web.run_app(app)

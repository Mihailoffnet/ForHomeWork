import pydantic
from flask import Flask, jsonify, request
from flask.views import MethodView
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError

from models import Session, User, Advert
from schema import CreateUser, UpdateUser, CreateAdvert, UpdateAdvert

app = Flask("app")
bcrypt = Bcrypt(app)


def hash_password(password: str):
    password = password.encode()
    return bcrypt.generate_password_hash(password).decode()


def check_password(password: str, hashed_password: str):
    password = password.encode()
    hashed_password = hashed_password.encode()
    return bcrypt.check_password_hash(password, hashed_password)


def validate(schema_class, json_data):
    try:
        return schema_class(**json_data).dict(exclude_unset=True)
    except pydantic.ValidationError as er:
        error = er.errors()[0]
        error.pop("ctx", None)
        raise HttpError(400, error)


class HttpError(Exception):
    def __init__(self, status_code: int, description: str):
        self.status_code = status_code
        self.description = description


@app.errorhandler(HttpError)
def error_handler(error: HttpError):
    response = jsonify({"error": error.description})
    response.status_code = error.status_code
    return response


@app.before_request
def before_request():
    session = Session()
    request.session = session


@app.after_request
def after_request(response):
    request.session.close()
    return response


def get_user_by_id(user_id: int):
    user = request.session.get(User, user_id)
    if user is None:
        raise HttpError(404, "user not found")
    return user


def get_advert_by_id(advert_id: int):
    advert = request.session.get(Advert, advert_id)
    if advert is None:
        raise HttpError(404, "advert not found")
    return advert


def add_user(user: User):
    try:
        request.session.add(user)
        request.session.commit()
    except IntegrityError as err:
        raise HttpError(409, "user already exists")
    return user

def add_advert(advert: Advert):
    try:
        request.session.add(advert)
        request.session.commit()
    except IntegrityError as err:
        raise HttpError(409, "advert already exists")
    return advert


class UserView(MethodView):
    def get(self, user_id: int):
        user = get_user_by_id(user_id)
        return jsonify(user.json)

    def post(self):
        json_data = validate(CreateUser, request.json)
        json_data["password"] = hash_password(json_data["password"])
        user = User(**json_data)
        add_user(user)
        response = jsonify(user.json)
        response.status_code = 201
        return response

    def patch(self, user_id: int):
        json_data = validate(UpdateUser, request.json)
        if "password" in json_data:
            json_data["password"] = hash_password(json_data["password"])
        user = get_user_by_id(user_id)
        for field, value in json_data.items():
            setattr(user, field, value)
        add_user(user)
        return jsonify(user.json)

    def delete(self, user_id: int):
        user = get_user_by_id(user_id)
        request.session.delete(user)
        request.session.commit()
        return jsonify({"status": "success"})


user_view = UserView.as_view("user_view")

class AdvertView(MethodView):
    def get(self, advert_id: int):
        advert = get_advert_by_id(advert_id)
        return jsonify(advert.json)

    def post(self):
        json_data = validate(CreateAdvert, request.json)
        advert = Advert(**json_data)
        add_advert(advert)
        response = jsonify(advert.json)
        response.status_code = 201
        return response

    def patch(self, advert_id: int):
        json_data = validate(UpdateAdvert, request.json)
        advert = get_advert_by_id(advert_id)
        for field, value in json_data.items():
            setattr(advert, field, value)
        add_advert(advert)
        return jsonify(advert.json)

    def delete(self, advert_id: int):
        advert = get_advert_by_id(advert_id)
        request.session.delete(advert)
        request.session.commit()
        return jsonify({"status": "success"})


advert_view = AdvertView.as_view("advert_view")

app.add_url_rule(
    "/user",
    view_func=user_view,
    methods=["POST",],)
app.add_url_rule(
    "/user/<int:user_id>", 
    view_func=user_view, 
    methods=["GET", "PATCH", "DELETE"],)
app.add_url_rule(
    "/advert",
    view_func=advert_view,
    methods=["POST",],)
app.add_url_rule(
    "/advert/<int:advert_id>", 
    view_func=advert_view, 
    methods=["GET", "PATCH", "DELETE"],)

app.run()

import pydantic
from flask import Flask, jsonify, request
from flask.views import MethodView
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError

from models import Session, Advert
from schema import CreateAdvert, UpdateAdvert

app = Flask("app")
bcrypt = Bcrypt(app)


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


def get_advert_by_id(advert_id: int):
    advert = request.session.get(Advert, advert_id)
    if advert is None:
        raise HttpError(404, "advert not found")
    return advert

def add_advert(advert: Advert):
    try:
        request.session.add(advert)
        request.session.commit()
    except IntegrityError as err:
        raise HttpError(409, "advert already exists")
    return advert


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
        return jsonify({"status": "advert updated"})

    def delete(self, advert_id: int):
        advert = get_advert_by_id(advert_id)
        request.session.delete(advert)
        request.session.commit()
        return jsonify({"status": "advert deleted"})


advert_view = AdvertView.as_view("advert_view")

app.add_url_rule(
    "/advert",
    view_func=advert_view,
    methods=["POST",],)
app.add_url_rule(
    "/advert/<int:advert_id>", 
    view_func=advert_view, 
    methods=["GET", "PATCH", "DELETE"],)

app.run()

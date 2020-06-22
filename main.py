from logic.api import Api
from flask import Flask, request
from flask_cors import CORS

import json

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

CORS(app)
api = Api()


def json_response(data, status=200):
    return json.dumps(data), status, {'Content-Type': 'application/json'}


@app.route('/')
def app_works():
    return json_response("server works")


@app.route('/form_wallpaper/form_wallpaper', methods=['POST'])
def calc_wallpaper():
    return json_response(api.calc_wallpapers(json.loads(request.data)))


@app.route('/form_tile/', methods=['POST'])
def calc_tile():
    return json_response(api.calc_tile(json.loads(request.data)))


@app.route('/form_paint/', methods=['POST'])
def calc_paint():
    return json_response(api.calc_paint(json.loads(request.data)))


@app.route('/form_laminate/', methods=['POST'])
def calc_laminate():
    return json_response(api.calc_laminate(json.loads(request.data)))


@app.route('/form_linoleum/', methods=['POST'])
def calc_linoleum():
    return json_response(api.calc_linoleum(json.loads(request.data)))


# app.run()
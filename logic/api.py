from db import DbClient
import math


class Api:
    def __init__(self):
        self.db_client = DbClient()

    def calc_wallpapers(self, params):
        params['material_length'] = 10.05
        params['material_width'] = 0.53
        if not params:
            params = self.db_client.get_values('wallpapers')
        square = self.calc_wall_square(params)
        return math.ceil(square / (params['material_length'] * params['material_width'])) + 1

    def calc_tile(self, params):
        if params['place'] == 'walls':
            if not params.get('material_length'):
                params = self.db_client.get_values('wall_tile')
            square = self.calc_wall_square(params)
        else:
            if not params.get('material_length'):
                params = self.db_client.get_values('floor_tile')
            square = self.calc_room_square(params)
        return math.ceil(square / (params['material_length'] * params['material_width']) * 1.1)

    def calc_paint(self, params):
        if params['place'] == 'walls':
            if not params.get('material_length'):
                params = self.db_client.get_values('wall_paint')
            square = self.calc_wall_square(params)
        else:
            if not params.get('material_length'):
                params = self.db_client.get_values('floor_paint')
            square = self.calc_room_square(params)
        return math.ceil(square / 8)

    def calc_laminate(self, params):
        if not params:
            params = self.db_client.get_values('laminate')
        square = self.calc_room_square(params)
        return math.ceil(square / (params['material_length'] * params['material_width'])) + 1

    def calc_linoleum(self, params):
        if not params:
            params = self.db_client.get_values('linoleum')
        return math.ceil(params['length'] / 20)

    @staticmethod
    def calc_wall_square(params):
        square = (params.get('width') + params.get('length')) * params.get('height') * 2
        square -= params.get('window_width') * params.get('window_height') * params.get('window_count')
        square -= params.get('door_width') * params.get('door_height')
        return square

    @staticmethod
    def calc_room_square(params):
        return params.get('width') * params.get('length')

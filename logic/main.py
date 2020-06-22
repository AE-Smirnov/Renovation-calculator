from api import Api


class Main:
    def __init__(self):
        self.api = Api()

    def calc_wallpaper(self, params):
        return self.api.calc_wallpapers(params)

    def calc_tile(self, params):
        return self.api.calc_tile(params)

    def calc_paint(self, params):
        return self.api.calc_paint(params)

    def calc_laminate(self, params):
        return self.api.calc_laminate(params)

    def calc_linoleum(self, params):
        return self.api.calc_linoleum(params)


if __name__ == '__main__':
    pass
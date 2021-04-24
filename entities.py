from random import randint
from pygame.draw import rect
from pygame import Rect
import json

cfg_data = json.load(open("game_config.json", "r"))
GENOTYPE_LEN = cfg_data["GENOTYPE_LEN"]  # кол-во генов
GEN_LEN = cfg_data["GEN_LEN"]  # длина гена в битах (закодированного)


def generate_random_genotype():
    ans = 0

    for i in range(GENOTYPE_LEN):
        ans += randint(0, (1 << GEN_LEN) - 1) << i*GEN_LEN

    return ans, GENOTYPE_LEN, GEN_LEN


def get_start_props():
    return json.load(open("start_properties.json", "r"))


class Animal:

    # класс особи

    genotype = 0
    genotype_len = 0
    gen_len = 0

    properties = dict()

    def __init__(self, **kwargs):

        # генерируем геном стартовый
        self.genotype, self.genotype_len, self.gen_len = generate_random_genotype()

        self.set_default_props()

        # неплохо было бы обработчик ошибок прикрутить на kwargs
        for key, value in kwargs.items():
            if key in self.properties.keys():
                self.properties[key] = value
            else:
                self.properties.update({key: value})

    def set_default_props(self):
        self.properties = {
            "pos": (0, 0),
            "age": 0,
            "hp": 100,
            "pix_by_x": 10
        }

    def update(self, env):

        for i in range(self.genotype_len):
            attr = (self.genotype >> (i*self.gen_len)) & ((1 << GEN_LEN) - 1)  # декодируем геном

        # TODO:прописать логику для особи

        # TODO:изменяем генотип (мутации)

    def draw(self, screen):
        sh = Rect(self.properties["pos"][0] * self.properties["pix_by_x"],
                  self.properties["pos"][1] * self.properties["pix_by_x"],
                  self.properties["pix_by_x"], self.properties["pix_by_x"])
        rect(screen, (255, 0, 0), sh)
        # TODO: сделать отрисовку особи
        pass

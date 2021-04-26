from random import randint
from pygame.draw import rect
from pygame import Rect
import json

cfg_data = json.load(open("game_config.json", "r"))
GENOTYPE_LEN = cfg_data["GENOTYPE_LEN"]  # кол-во генов
GEN_LEN = cfg_data["GEN_LEN"]  # длина гена в битах (закодированного)
BLOCK_SIZE = cfg_data["BLOCK_SIZE"]


def mutate(genotype):
    i = randint(0, GENOTYPE_LEN - 1)
    p = randint(0, GEN_LEN - 1)
    return genotype ^ (1 << (i * GEN_LEN) + p)


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

    def __init__(self, gen, **kwargs):

        if gen is None:
            # если стартовая особь
            self.genotype, self.genotype_len, self.gen_len = generate_random_genotype()
        else:
            # если чей-то потомок
            self.genotype, self.genotype_len, self.gen_len = gen, GENOTYPE_LEN, GEN_LEN

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
            "hp": 10,
            "feed": 10,
            "pix_by_x": BLOCK_SIZE,
            "endurance": 1,
            "fit": 0  # уровень приспособленности особи (ВАЖНО)
        }

    def get_fen(self, pos):
        # получаем данный фенотип из генома по позиции с конца
        return (self.genotype >> (pos*self.gen_len)) & ((1 << self.gen_len) - 1)

    def update(self, env):

        for i in range(self.genotype_len):
            attr = (self.genotype >> (i*self.gen_len)) & ((1 << GEN_LEN) - 1)  # декодируем геном
            value = self.get_fen(i)

            if value == 1:
                p = self.properties["pos"]
                p_2 = (p[0], p[1]+1)
                if env.move(p, p_2):
                    self.properties["pos"] = p_2
            if value == 2:
                p = self.properties["pos"]
                p_2 = (p[0], p[1]-1)
                if env.move(p, p_2):
                    self.properties["pos"] = p_2
            if value == 3:
                p = self.properties["pos"]
                p_2 = (p[0]+1, p[1])
                if env.move(p, p_2):
                    self.properties["pos"] = p_2
            if value == 4:
                p = self.properties["pos"]
                p_2 = (p[0]-1, p[1])
                if env.move(p, p_2):
                    self.properties["pos"] = p_2

            if value == 5:
                # едим с земли
                self.properties["feed"] += env.get_food(self.properties["pos"])
            if value == 6:
                # питаемся фотосинтезом
                self.properties["feed"] += env.get_photosyn(self.properties["pos"])

            if value == 7:
                # размножение
                if self.properties["hp"] > 7:
                    env.clone(self.properties["pos"])

        self.properties["feed"] -= 1
        if self.properties["feed"] < 0:
            self.properties["hp"] -= 1

        if self.properties["hp"] <= 0:
            env.kill(self.properties["pos"])

    def draw(self, screen):
        sh = Rect(self.properties["pos"][0] * self.properties["pix_by_x"],
                  self.properties["pos"][1] * self.properties["pix_by_x"],
                  self.properties["pix_by_x"], self.properties["pix_by_x"])
        rect(screen, (255, 0, 0), sh)
        # TODO: сделать отрисовку особи
        pass

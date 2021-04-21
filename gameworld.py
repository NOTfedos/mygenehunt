from random import randint
import json

from instructions import animal_action


START_ANIMAL_COUNT = 50  # кол-во особей начальное
GENOTYPE_LEN = 16  # кол-во генов
GEN_LEN = 4  # длина гена в битах (закодированного)


def generate_random_genotype():
    ans = 0

    for i in range(GENOTYPE_LEN):
        ans += randint(0, (1 << GEN_LEN) - 1) << i*GEN_LEN

    return ans, GENOTYPE_LEN, GEN_LEN


def get_start_props():
    return json.load(open("start_properties.json", "r"))


class Animal:
    genotype = 0
    genotype_len = 0
    gen_len = 0

    properties = dict()


    def __init__(self):

        # генерируем геном стартовый
        self.genotype, self.genotype_len, self.gen_len = generate_random_genotype()

        # получаем характеристики особи (стартовые)
        self.properties = get_start_props()


    def update(self, env):

        for i in range(self.genotype_len):
            attr = (self.genotype >> (i*self.gen_len)) & ((1 << GEN_LEN) - 1)  # декодируем геном

            animal_action(self, i, attr)


class Game:

    animal_list = []
    ended = False


    def __init__(self, animal_count, **kwargs):

        # animal_instructions = json.load(open("animal_instructions.json", "r"))

        for i in range(animal_count):
            self.animal_list.append(Animal())


    def update(self, screen, **kwargs):
        if self.ended:
            return

        # нарисуем фон

        # обновим окружение

        # нарисуем окружение

        # обновим состояния особей

        # нарисуем особей

        pass


    def end(self, **kwargs):
        self.ended = True


game = Game(START_ANIMAL_COUNT)

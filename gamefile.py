import json
from random import randint
from entities import Animal
from animal_env import AnimalEnv

cfg_data = json.load(open("game_config.json", "r"))
START_ANIMAL_COUNT = cfg_data["START_ANIMAL_COUNT"]  # кол-во особей начальное
FIELD_SIZE = tuple(cfg_data["FIELD_SIZE"])  # приводим к неизменяемому типу размер игрового поля
BLOCK_SIZE = cfg_data["BLOCK_SIZE"]  # размер ячейки поля


class Game:

    animal_list = []
    ended = False
    env = None

    def __init__(self, animal_count, **kwargs):

        for i in range(animal_count):
            self.animal_list.append(Animal(
                pos=(randint(0, FIELD_SIZE[0]), randint(0, FIELD_SIZE[1])),
                pix_by_x=BLOCK_SIZE
            ))

        self.env = AnimalEnv(FIELD_SIZE)

    def update(self, screen, **kwargs):
        if self.ended:
            return

        # нарисуем фон -> сейчас рисуется в окружении

        self.env.update()  # обновим окружение

        self.env.draw(screen)  # нарисуем окружение

        for animal in self.animal_list:
            animal.update(self.env)  # обновим состояния особей
            animal.draw(screen)  # нарисуем особей

    def end(self, **kwargs):
        self.ended = True


game = Game(START_ANIMAL_COUNT)

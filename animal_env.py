from pygame.draw import rect
from pygame import Rect


class AnimalEnv:

    # содержит в себе 2D карту мира (по умолчанию заполняется None)

    env_map = []

    def __init__(self, size):
        self.env_map = [[None for _ in range(size[1])] for _ in range(size[0])]

    def put_element(self, el, pos):
        self.env_map[pos[0]][pos[1]] = el

    def remove_element(self, pos):
        self.env_map[pos[0]][pos[1]] = None

    def get_element(self, pos):
        return self.env_map[pos[0]][pos[1]]

    def draw(self, screen):
        # TODO:сделать отрисовку игрового поля

        rect(screen, (255, 255, 255), Rect((0, 0), screen.get_size()))

        pass

    def update(self):
        # TODO: обновление окружения
        pass

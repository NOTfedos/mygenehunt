from pygame.draw import rect
from pygame import Rect
from entities import Animal, mutate


class AnimalEnv:

    # содержит в себе 2D карту мира (по умолчанию заполняется None)

    env_map = []
    food_map = []
    size = tuple()

    def __init__(self, size):
        self.env_map = [[None for _ in range(size[1])] for _ in range(size[0])]
        self.food_map = [[1 for _ in range(size[1])] for _ in range(size[0])]
        self.size = size

    def put_element(self, el, pos):
        self.env_map[pos[0]][pos[1]] = el

    def remove_element(self, pos):
        self.env_map[pos[0]][pos[1]] = None

    def get_element(self, pos):
        return self.env_map[pos[0]][pos[1]]

    def move(self, pos1, pos2):
        # перемещаем объект из pos1 в pos2

        if pos2[0] > self.size[0] or pos2[0] < 0:
            return False

        if pos2[1] > self.size[1] or pos2[1] < 0:
            return False

        if self.env_map[pos2[0]][pos2[1]] is None:
            c = self.env_map[pos1[0]][pos1[1]].copy()
            self.env_map[pos1[0]][pos1[1]] = None
            self.env_map[pos2[0]][pos2[1]] = c
            return True
        return False

    def clone(self, pos):
        animal = self.get_element(pos)

        x, y = pos

        if (x + 1 < self.size[0]) and (self.get_element((x + 1, y)) is None):
            self.env_map[x + 1][y] = Animal(mutate(animal.genotype), pos=(x+1, y))

        if (x - 1 > 0) and (self.get_element((x - 1, y)) is None):
            self.env_map[x - 1][y] = Animal(animal.genotype, pos=(x-1, y))

        if (y + 1 < self.size[0]) and (self.get_element((x, y + 1)) is None):
            self.env_map[x][y + 1] = Animal(animal.genotype, pos=(x, y+1))

        if (y - 1 > 0) and (self.get_element((x, y - 1)) is None):
            self.env_map[x][y - 1] = Animal(animal.genotype, pos=(x, y-1))

    def draw(self, screen):
        # TODO:сделать отрисовку игрового поля
        rect(screen, (255, 255, 255), Rect((0, 0), screen.get_size()))

    def update(self):
        # вырастим еду
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                self.food_map[x][y] += 0.1

    def get_food(self, pos):

        ans = self.food_map[pos[0]][pos[1]]
        self.food_map[pos[0]][pos[1]] -= 1

        return ans

    def get_photosyn(self, pos):
        return 10 * pos[1] / self.size[1]

    def kill(self, pos):
        self.env_map[pos[0]][pos[1]] = None

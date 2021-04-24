import pygame
from gamefile import game
import json


cfg_data = json.load(open("game_config.json", "r"))
SCREEN_SIZE = cfg_data["SCREEN_SIZE"]


def main():
    pygame.init()
    running = True

    screen = pygame.display.set_mode(SCREEN_SIZE)

    # игровой цикл
    while running:

        # обработаем события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        game.update(screen)

        # обновим картинку
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

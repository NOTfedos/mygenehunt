import pygame
from gameworld import game


def main():
    pygame.init()
    running = True

    screen = pygame.display.set_mode((1600, 900))

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
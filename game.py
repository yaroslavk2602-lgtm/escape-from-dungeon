import pygame
import time

pygame.init()

# Размеры окна
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

# FPS
FPS = 60

# Цвета
BLACK = (0, 0, 0)
DARK_GRAY = (40, 40, 40)

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Escape from Dungeon")

clock = pygame.time.Clock()

# Внутриигровое время
start_time = time.time()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Подсчёт времени игры
    elapsed_time = time.time() - start_time

    # Отрисовка игрового пространства
    screen.fill(DARK_GRAY)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

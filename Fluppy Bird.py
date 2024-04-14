import pygame
import sys

pygame.init()

# Определение основных переменных
window_width = 600
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Flappy Bird Clone')

background_color = (135, 206, 250)
bird_color = (255, 165, 0)
bird_width = 40
bird_height = 30
bird_x = 50
bird_y = 200
bird_speed = 0
gravity = 0.25

# Функция отрисовки птицы
def draw_bird(x, y):
    pygame.draw.rect(window, bird_color, (x, y, bird_width, bird_height))

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = -5

    # Применение гравитации
    bird_speed += gravity
    bird_y += bird_speed

    # Очистка экрана и отрисовка фона
    window.fill(background_color)

    # Отрисовка птицы
    draw_bird(bird_x, bird_y)

    pygame.display.update()
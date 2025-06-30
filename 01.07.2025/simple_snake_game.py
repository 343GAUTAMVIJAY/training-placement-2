import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
snake = [(400, 300)]
food = (random.randint(0, 79) * 10, random.randint(0, 59) * 10)
direction = (10, 0)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction[1] == 0:
                direction = (0, -10)
            elif event.key == pygame.K_DOWN and direction[1] == 0:
                direction = (0, 10)
            elif event.key == pygame.K_LEFT and direction[0] == 0:
                direction = (-10, 0)
            elif event.key == pygame.K_RIGHT and direction[0] == 0:
                direction = (10, 0)
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if head == food:
        food = (random.randint(0, 79) * 10, random.randint(0, 59) * 10)
    else:
        snake.pop()
    snake.insert(0, head)
    if head[0] < 0 or head[0] >= 800 or head[1] < 0 or head[1] >= 600 or head in snake[1:]:
        pygame.quit()
        exit()
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (*food, 10, 10))
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, 10, 10))
    pygame.display.flip()
    clock.tick(10)
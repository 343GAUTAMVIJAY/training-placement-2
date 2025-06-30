import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
paddle = pygame.Rect(50, 250, 20, 100)
ball = pygame.Rect(400, 300, 20, 20)
ball_speed = [5, 5]
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle.top > 0:
        paddle.y -= 5
    if keys[pygame.K_DOWN] and paddle.bottom < 600:
        paddle.y += 5
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
    if ball.top <= 0 or ball.bottom >= 600:
        ball_speed[1] = -ball_speed[1]
    if ball.colliderect(paddle):
        ball_speed[0] = -ball_speed[0]
    if ball.left <= 0:
        ball.x, ball.y = 400, 300
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    pygame.draw.rect(screen, (255, 255, 255), ball)
    pygame.display.flip()
    clock.tick(60)
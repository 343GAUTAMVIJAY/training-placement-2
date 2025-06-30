import random

width, height = 10, 10
maze = [['#' for _ in range(width)] for _ in range(height)]
x, y = 1, 1
maze[y][x] = ' '
for _ in range(50):
    dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
    nx, ny = x + dx*2, y + dy*2
    if 0 < nx < width-1 and 0 < ny < height-1:
        maze[ny][nx] = maze[y+dy][x+dx] = ' '
        x, y = nx, ny
for row in maze:
    print(''.join(row))
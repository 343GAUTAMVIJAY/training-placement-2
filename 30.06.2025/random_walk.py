import random

x, y = 0, 0
steps = int(input("Enter number of steps: "))
for _ in range(steps):
    direction = random.choice(['up', 'down', 'left', 'right'])
    if direction == 'up':
        y += 1
    elif direction == 'down':
        y -= 1
    elif direction == 'left':
        x -= 1
    elif direction == 'right':
        x += 1
print(f"Final position: ({x}, {y})")
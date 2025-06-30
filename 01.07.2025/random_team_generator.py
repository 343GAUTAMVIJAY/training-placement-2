import random

names = input("Enter names (comma-separated): ").split(',')
random.shuffle(names)
team_size = len(names) // 2
print("Team 1:", names[:team_size])
print("Team 2:", names[team_size:])
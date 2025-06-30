import random

numbers = list(range(1, 5)) * 2
random.shuffle(numbers)
revealed = ['_'] * 8
matches = 0
while matches < 4:
    print(' '.join(map(str, revealed)))
    pos1 = int(input("Enter first position (1-8): ")) - 1
    pos2 = int(input("Enter second position (1-8): ")) - 1
    if numbers[pos1] == numbers[pos2]:
        revealed[pos1] = revealed[pos2] = numbers[pos1]
        matches += 1
    else:
        print(f"{numbers[pos1]} and {numbers[pos2]} don't match!")
print("You win!")
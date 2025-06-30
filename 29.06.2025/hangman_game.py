import random

words = ['python', 'coding', 'game', 'hangman']
word = random.choice(words)
guessed = ['_'] * len(word)
attempts = 6
while attempts > 0 and '_' in guessed:
    print(' '.join(guessed), f"Attempts left: {attempts}")
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        attempts -= 1
print("You win!" if '_' not in guessed else f"You lose! Word was {word}")
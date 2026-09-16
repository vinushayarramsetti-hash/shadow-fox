
import random

words = {
    "python": "A popular programming language",
    "computer": "An electronic machine",
    "developer": "A person who creates software",
    "internet": "A global network",
    "program": "A set of instructions"
}

hangman = [
"""
  +---+
      |
      |
      |
     ===
""",
"""
  +---+
  O   |
      |
      |
     ===
""",
"""
  +---+
  O   |
  |   |
      |
     ===
""",
"""
  +---+
  O   |
 /|   |
      |
     ===
""",
"""
  +---+
  O   |
 /|\\  |
      |
     ===
""",
"""
  +---+
  O   |
 /|\\  |
 /    |
     ===
""",
"""
  +---+
  O   |
 /|\\  |
 / \\  |
     ===
"""
]

word = random.choice(list(words.keys()))
hint = words[word]

guessed = []
wrong_guesses = 0
max_wrong = 6

print("================================")
print("        HANGMAN GAME")
print("================================")

print("\nHint:", hint)

while wrong_guesses < max_wrong:

    print(hangman[wrong_guesses])

    display = ""

    for letter in word:

        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)

    if "_" not in display:
        print("\n🎉 CONGRATULATIONS!")
        print("You guessed the word:", word)
        break

    print("Wrong guesses:", wrong_guesses)
    print("Remaining chances:", max_wrong - wrong_guesses)

    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed:
        print("You already guessed this letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("✅ Correct!")

    else:
        print("❌ Wrong!")
        wrong_guesses += 1

else:

    print(hangman[wrong_guesses])

    print("\nGAME OVER!")
    print("The correct word was:", word)
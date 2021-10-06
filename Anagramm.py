import random
WORDS = ("test", "python", "programming")
word = random.choice(WORDS)
correct = word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print("Welcome to the \"Anagramms!\"\nyour anagramm: " + jumble)
guess = input("\nTry to guess: ")
while guess != correct and guess != "":
    print("You are wrong, try one more time")
    guess = input("\nTry to guess: ")
if guess == correct:
    print("Congratulations!")
input("\n\nPress Enter to exit.")
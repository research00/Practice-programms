import random
WORDS = {"exam": "something you have to pass to graduate school",
         "python": "both a language and a snake",
         "programming": "a process of writing code",
         "goat": "an animal with small horns",
         "thing": "all you can think of"}
word = random.choice(list(WORDS.keys()))
correct = word
jumble = ""
score = 0
number_of_tries = 0
hint = 0
#score goes to 1000 if the player didn't ask for a hint and 600 if did

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print("Welcome to the \"Anagramms!\"\nyour anagramm: " + jumble)
guess = input("\nTry to guess: ")
while guess != correct and guess != "":
    number_of_tries += 1
    guess = input("Not quite there yet. Type \"yes\" if you would like a hint\n")
    if guess == "yes" or guess == "Yes" or guess == "YES":
        hint = 1
        print(WORDS.get(correct))
        guess = input("\nTry to guess: ")
    elif guess == "no" or guess == "No" or guess == "NO":
        guess = input("\nThat's the spirit! Try to guess: ")
if guess == correct:
    print("Congratulations! You finally guessed it right.\n")

    score = 1000 - (number_of_tries)*100 - hint*200
    if score < 0:
        score = 0
    if score < 500:
        print("Looks like your score is ", end = '')
        print(score)
        print("At first I thought you could do better. If that is your best...")
    elif score == 0:
        print("Looks like your score is ", end = '')
        print(score)
        print("There's no way you aren't kidding me...")
    elif score >= 500 and score < 900:
        print("Looks like your score is ", end = '')
        print(score)
        print("Don't get me wrong, I'm not impressed. But I've seen worse.")
    else:
        print("Looks like your score is ", end='')
        print(score)
        print("Nice! You did a good job!")
input("\n\n\nPress Enter to exit.")
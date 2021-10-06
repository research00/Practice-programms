import random
the_number = random.randint(1, 100)
guess = int(input("Your guess: "))
tries = 1
while guess != the_number:
    if guess > the_number:
        print("Smaller...")
    else:
        print("Larger...")
    guess = int(input("Your guess: "))
    tries += 1
print("You are right! You only needed " + str(tries) + " tries")
input("\n\n Press Enter to exit. ")
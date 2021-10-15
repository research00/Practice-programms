import random
import csv

print('{:*^120}'.format(' Welcome to the \"HANGMAN\"! '))
print(
    """
      You will have to guess the word my powerful computer mind has riddled.
    """
)
# creating a constant tuple of images the programm needs to print
HANGMAN = ("""
            -------=-
            |      |
            |      |
            |   
            |   
            |    
            |  
            |  
            |     
            |     
            |     
            |
           ------------
           """,
           """
            -------=-
            |      |
            |      |
            |      O
            |  
            |   
            |        
            |
            |     
            |     
            |     
            |
           ------------
           """,
           """
            -------=-
            |      |
            |      |
            |      O
            |     -+-
            |     
            |    
            |    
            |    
            |    
            |     
            |
           ------------
           """,
           """
            -------=-
            |      |
            |      |
            |      O
            |     -+-
            |    /  
            |     
            |     
            |     
            |     
            |     
            |
           ------------
           """,
           """
            -------=-
            |      |
            |      |
            |      O
            |     -+-
            |    /   \ 
            |      
            |     
            |     
            |     
            |     
            |
           ------------
           """,
           """
            -------=-
            |      |
            |      |
            |      O
            |     -+-
            |    / | \ 
            |     
            |     
            |     
            |     
            |     
            |
           ------------
           """,
           """
            -------=-
            |      |
            |      |
            |      O
            |     -+-
            |    / | \ 
            |      |
            |     
            |     
            |     
            |     
            |
           ------------
           """,
           """
            -------=-
            |      |
            |      |
            |      O
            |     -+-
            |    / | \ 
            |      |
            |     | 
            |     | 
            |     | 
            |     
            |
           ------------
           """,

           """
            -------=-
            |      |
            |      |
            |      O
            |     -+-
            |    / | \ 
            |      |
            |     | |
            |     | |
            |     | |
            |     
            |
           ------------
           """,
           )
# as soon as the programm starts there is already the first picture, so the maximum number of mistakes  
# should be lowered by 1
MAX_WRONG = len(HANGMAN) - 1
# opening a csv file and reading the words for the game
with open("hangman words.csv", "r") as file1:
    reader = csv.reader(file1)
    WORDSl = []
    for row in reader:
        WORDSl.append(row)
# WORDSl keeps the words as a list of lists, so we need to convert it to a tuple of values, which will be WORDS

WORDS = ()
# converting list of lists to a list of values forced to upper case
for i in range(len(WORDSl)):
    WORDSl[i] = WORDSl[i][0].upper()
# copying the list to a tuple
WORDS = WORDSl[:]
word = random.choice(WORDS)
so_far = "-"*len(word)
wrong = 0
used = []

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou have suggested these letters: \n",used)
    print("The word you are trying to guess looks like that now: ", so_far)
    guess = input("\n\nEnter a letter: ")
    guess = guess.upper()
    while guess in used:
        print("You already suggested the letter", guess)
        guess = input("\n\nEnter a letter: ")
        guess = guess.upper()
    used.append(guess)
    if guess in word:
        print("\nYes there is a letter", guess, "in this word!")
# creating a string with guessed letters and "-"s
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nUnfortunately, there is no letter", guess, "in this word")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou were hanged.")
else:
    print("\nYou guessed it right!")
print("\nThe word was", word)
input("Нажмите Enter для выхода.")
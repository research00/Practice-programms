# another demonstration of list methods
# SCORES 2_0
scores = []
choice = None
while choice != "0":
    print(
        '''
        0 - Exit
        1 - Show top scores
        2 - Add a score
        '''
    )
    choice = input("Your choice: \n")
    if choice == '0':
        print("Goodbye")
    elif choice == '1':
        print('Top scores: \n')
        print("NAME\tRESULT")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
    elif choice == '2':
        name = input("Enter your nickname: ")
        score = int(input("Enter your score: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
    else:
        print("There is no such option in the menu as", choice, ", please choose an item from the menu")

input("\nPress Enter too exit.")
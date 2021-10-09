# another demonstration of list methods
scores = []
choice = None
while choice != "0":
    print(
        '''
        0 - Exit
        1 - Show top scores
        2 - Add a score
        3 - Delete a score
        4 - Sort the score list
        '''
    )
    choice = input("Your choice: ")
    if choice == '0':
        print("Goodbye")
    elif choice == '1':
        print("Top scores:")
        for score in scores:
            print(score, end = ';   ')
    elif choice == '2':
        score = int(input("Enter your score: "))
        scores.append(score)
    elif choice == '3':
        score = int(input("Enter the score you want to remove: "))
        if score in scores:
            scores.remove(score)
        else:
            print("There's no such score on the list.")
    elif choice == '4':
        scores.sort(reverse=True)
    else:
        print("There is no such option in the menu as", choice, ", please choose an item from the menu")

input("\nPress Enter too exit.")
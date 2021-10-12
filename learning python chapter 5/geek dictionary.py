# geek dictionary programm
# illustrates the capabilities of the dictrionary type


geek = {'404': 'Information not found',
        'Googling': 'Finding information online',
        'Percussive maintenance':'Fixing something with hitting it',
        'Uninstalled': 'When someone is fired'
        }
choice = None
while choice != 0:
    print(
    '''
    Geek - English Dictionary
    0 - Exit
    1 - Find a definition
    2 - Add a term
    3 - Change a definition
    4 - Delete a term
    
    '''
    )
    choice = int(input("Your choice: "))
    if choice == 0:
        print("Goodbye.\n")
    elif choice == 1:
        term = input("What term do you want to define? ")
        if term in geek:
            definition = geek[term]
            print("\n", term, "means", definition)
        else:
            print("\nI am not familiar with this term.")
    elif choice == 2:
        term = input("What term do you want to add? ")
        if term not in geek:
            definition = input("\nExplain the term: ")
            geek[term] = definition
            print("\nThe term ", term, "was added to the dictionary.")
        else:
            print("\nThis term is already in the dictionary.")
    elif choice == 3:
        term = input('What term do you want to redefine? ')
        if term in geek:
            definition = input("\nDefine the term: ")
            geek[term] = definition
            print("\nThe term ", term, "was redefined.")
        else:
            print("\nThis term is not in the dictionary.")
    elif choice == 4:
        term = input('What term do you want to delete? ')
        if term in geek:
            del geek[term]
            print("\nThe term ", term, "was deleted.")
        else:
            print("\nThis term is not in the dictionary.")
    else:
        print("There is no such option in the menu. Please select an option from the menu. ")
input("\n\nPress \"Enter\" to exit.")
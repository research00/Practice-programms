#Hero's inventory 3.0 (LISTS)
inventory = ["sword", "armor", "shield", "healing potion"]
print("You have the following items in your inventory: ")
i = 0
for item in inventory:
    i += 1
    print(i, end = '')
    print(".", item)
print("\nFor now you have", len(inventory), "items")

if "healing potion" in inventory:
    print("\nYou still have some time to live and to fight.")

#slicing capabilities of lists
start = 1
finish = 4
print("\nItems in the inventory from", start, "to", finish, ": \n")
print(inventory[start:finish])

#adding capabilities of lists
chest = ["gold", "gems"]
print("\nYou found the chest with the following items: ")
print(chest)

inventory += chest
print("\nYou took these items. Now your inventory looks like this: ")
print(inventory)

#indexation capabilities of lists
inventory[0] = "crossbow"
print("\nYou traded a sword for a crossbow. Now you have: ")
print(inventory)

#replacing several elements with one
inventory[4:6] = ["magical orb"]
print("\nYou traded gold and gems for a magical orb capable of predicting future. Now you have: ")
print(inventory)

#deleting an element by it's index or with a slice
del inventory[2]
print("\nYour shield was destroyed in a fight. Now you have: ")
print(inventory)

del inventory[:2]
print("\nYou were robbed! Thieves stole your armor and crossbow. All you have left is: ")
print(inventory)
input("\nPress Enter to exit.")


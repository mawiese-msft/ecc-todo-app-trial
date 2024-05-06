todo_list = []

# Print the menu
print() # Add a couple of blank lines
print("Actions:")
print("A - Add to-do item")
print("R - Remove to-do item")     #<--- ***HERE***
print("X - Exit")
print("P - Print to-do list")
print("S - Sort to-do list in alphabetical order")

#continue to loop and display menu until user selects to exit the program
while True:
    
    choice = input("Enter your choice (A, R, P, S, or X): ")  #<--- ***ALSO UPDATE MENU OPTIONS with the 'R' ***
    choice = choice.upper() #converts the choice to uppercase

    #user selected 'a' or 'A' - To Add an item to the list
    if choice == "A":
        todo = input("Enter the to-do item: ") 
        todo_list.append(todo)
        continue  #tells the program to go back to the start of the loop

    #user selected 'r' or 'R' - To Remove an item from the list
    if choice == "R":
        item_number = int(input("Enter the number of the item to remove: "))
        if item_number > 0 and item_number <= len(todo_list):
            todo_list.pop(item_number - 1)
        else:
            print("Invalid item number")
        continue

    if choice == "P":
        print() # Add a couple of blank lines
        print("To-do list: ") # Print the title of the list
        for todo in todo_list: # Loop through existing to-do items
            print(todo)
        print()
        continue

    if choice == "S":
        todo_list.sort()
        print()
        print("To-do list is now sorted") 
        continue

    #user selected 'x' or 'X' to exit program
    if choice == "X":
        break #tells the program to exit the loop

    #user selected something else
    print("Invalid choice")
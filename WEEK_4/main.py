from Ques1 import Ques1
from Ques2 import Ques2
from Ques3 import Ques3
from Ques4 import Ques4

choice = 1
while choice != 0:

    open = input("Do you want to open the menu? (y/n): ")
    if open.lower() == 'y':
            print("\n------------------MENU------------------")
            print("All Questions: from WEEK_4")
            print("1. Ques 1: ")
            print("2. Ques 2: ")
            print("3. Ques 3: ")
            print("4. Ques 4: ")
            print("0. Exit")
    elif open.lower() == 'n':
        choice = 0
        print("Exiting...")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        continue
    
    try:
        choice = int(input("---------------Enter your Choice--------------- : "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        obj = Ques1()
        print(f"Sum: {obj.sum()}")
        print(f"Average: {obj.average()}")
    elif choice == 2:
        message = input("Enter a string to check if it's a palindrome: ")
        obj = Ques2(message)
        if obj.isPalindrome():
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")
    elif choice == 3:
        obj = Ques3()
        obj.highest_score()
    elif choice == 4:
        obj = Ques4()
        print(f"Numbers in decreasing order: {obj.decreasing_order()}")
        print(f"Numbers in increasing order: {obj.increasing_order()}")
        
    elif choice == 0:
        print("Exiting...")
    else:
        print("Invalid choice. Please try again.")
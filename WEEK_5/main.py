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
        obj.display()
    elif choice == 2:
        obj = Ques2()
        obj.operations()
    elif choice == 3:
        obj = Ques3()
        obj.display_prime()
    elif choice == 4:
        obj = Ques4()
        obj.array_indexing()
    elif choice == 0:
        print("Exiting...")
    else:
        print("Invalid choice. Please try again.")

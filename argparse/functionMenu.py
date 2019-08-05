def mainMenu():
    print("1. Do something good")
    print("2. Do something bad")
    print("3. Quit")
    while True:
        try:
            selection=int(input("Enter choice: "))
            if selection==1:
                good()
                break
            elif selection==2:
                bad()
                break
            elif selection==3:
                break
            else: 
                print("Invalid choice. Enter 1-3")
                mainMenu()
        except ValueError:
            print("Invalid choice. Enter 1-3")
    exit

def good():
    print("Good")
    anykey=input("Enter anything to return to main menu: ")
    mainMenu()

def bad():
    print("Bad")
    anykey=input("Enter anything to return to main menu: ")
    mainMenu()
        
#  main routine
mainMenu()
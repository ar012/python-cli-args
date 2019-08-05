def menu():
    print("Welcome, \n 1. Print Hello \n 2. Print World \n 3. Print Python \n 4. Print Hello World, welcome to my program")
    choice = input()

    if choice == "1":
        print("Hello")
        menu()

    if choice == "2":
        print("World")
        menu()

    if choice == "3":
        print("Python")
        menu()

    if choice == "4":
        print("Hello World, welcome to my program")
        menu()

menu()
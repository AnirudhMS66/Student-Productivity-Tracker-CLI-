count = 0

while True:
    print("\nMENU")
    print("1. Option One")
    print("2. Option Two")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    count += 1

    if choice == 1:
        print("You selected Option One")
    elif choice == 2:
        print("You selected Option Two")
    elif choice == 3:
        print("Exiting program...")
        print("Menu executed", count, "times")
        break
    else:
        print("Invalid choice")

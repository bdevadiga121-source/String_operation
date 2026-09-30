import sys

while True:
    print("\n STRING OPERATIONS")
    print("1. String Concatenation")
    print("2. String Replication")
    print("3. Exit")

    choice = input("Enter the choice: ")

    if choice == '1':
        print("1. String Concatenation")
        str1 = input("Enter the first string: ")
        str2 = input("Enter the second string: ")
        result = str1 + str2
        print("String concatenation: ",result)

    elif choice == '2':
        print("2. String Replication")
        str1 = input("Enter the string: ")
        number = int(input("Enter the number for repitition: "))

        result = str1 * number
        print("String Replication: ",result)

    elif choice == '3':
        print("Program terminated..............")
        sys.exit()

    else:
        print("Invalid choice.")



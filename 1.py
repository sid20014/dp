def encrypt(shift,password):
    cipherPassword=""
    for i in password:
        if i.isupper():
            cipherPassword+= chr((ord(i)+shift-65)%26+65)
        elif i.islower():
            cipherPassword+= chr((ord(i)+shift-97)%26+97)
        elif i.isdigit():
            cipherPassword+= i
        else:
            cipherPassword+= i
    return cipherPassword


def decrypt(shift,cipherPass):

    plainPassword=""

    for i in cipherPass:
        if i.isupper():
            plainPassword+= chr((ord(i)-shift-65)%26+65)
        elif i.islower():
            plainPassword+= chr((ord(i)-shift-97)%26+97)
        elif i.isdigit():
            plainPassword+= i
        else:
            plainPassword+= i
    return plainPassword

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice (1, 2, or 3): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            shift = int(input("Enter the shift ::"))
            password = input("Enter the password ::")
            cipherPass = encrypt(shift,password)
            print(cipherPass)
        elif choice == 2:
            shift = int(input("Enter the shift ::"))
            cipherPass = input("Enter the password ::")
            plainPassword = decrypt(shift,cipherPass)
            print(plainPassword)
        elif choice == 3:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
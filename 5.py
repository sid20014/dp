import random
def generatePassword(n):
    if(n<8):
        print("Password length should be greater than 8")
        return
    else:
        password=""

        with open("dic.txt", "r") as file:
            chars = file.read().splitlines()

        Up = [char for char in chars if char.isupper()]
        low = [char for char in chars if char.islower()]
        num = [char for char in chars if char.isdigit()]
        special = [char for char in chars if not char.isalnum()]



        password += random.choice(Up)
        password += random.choice(low)
        password += random.choice(num)
        password += random.choice(special)

        while len(password) < n:
            password += random.choice(chars)

        return password

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Generate Password.")
        print("2. Exit")

        try:
            choice = int(input("Enter your choice (1, 2): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            n = int(input("Enter the desired password length: "))
            password = generatePassword(n)
            print("Generated Password:", password)
        elif choice == 2:
            print("Exiting the program. Goodbye!")
            break


if __name__ == "__main__":
    main_menu()
def encryption(plaintext,numRails):

    rail=[["0" for i in range(len(plaintext))] for i in range(numRails)]

    direction = False
    row,col = 0,0


    for char in plaintext:
        rail[row][col]=char
        col+=1

        if row == 0 or row== numRails-1:
            direction = not direction

        if(direction):
            row+=1
        else:
            row-=1

    cipherText=[]
    for i in rail:
        for j in i:
            if j!="0":
                cipherText.append(j)
    return "".join(cipherText)


def decrypt(cipherText,numRails):
    rail=[["0" for i in range(len(cipherText))] for i in range(numRails)]

    direction = False
    row,col = 0,0

    for i in range(len(cipherText)):
        if row == 0:
            direction = True
        if row == numRails - 1:
            direction = False

        rail[row][col] = '*'
        col += 1

        if direction:
            row += 1
        else:
            row -= 1

    index=0
    for i in range(numRails):
        for j in range(len(cipherText)):
            if ((rail[i][j] == '*') and (index < len(cipherText))):
                rail[i][j] = cipherText[index]
                index+=1
    plainText=[]
    row,col=0,0
    for i in range(len(cipherText)):

        if row == 0:
            direction = True
        if row == numRails - 1:
            direction = False

        if rail[row][col] != '*':
            plainText.append(rail[row][col])
            col += 1

        if direction:
            row += 1
        else:
            row -= 1
    return "".join(plainText)


def main_menu():
    while True:
        print("\nMenu:")
        print("1. Encrypt....")
        print("2. Decrypt....")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice (1, 2,3): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            plaintext = input("Enter the plaintext ::")
            numRails = int(input("Enter the number of rails ::"))
            cipherText = encryption(plaintext,numRails)
            print(cipherText)
        elif choice == 2:
            cipherText = input("Enter the ciphertext ::")
            numRails = int(input("Enter the number of rails ::"))
            plainText = decrypt(cipherText,numRails)
            print(plainText)
        elif choice == 3:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")



if __name__ == "__main__":
    main_menu()
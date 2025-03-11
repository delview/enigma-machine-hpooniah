# Start Enigma Machine

# Phone charcters matching

phone_charcters_decrypt = {
"2": "A",
"22": "B",
"222": "C",
"3": "D",
"33": "E",
"333": "F",
"4": "G",
"44": "H",
"444": "I",
"5": "J",
"55": "K",
"555": "L",
"6": "M",
"66": "N",
"666": "O",
"7": "P",
"77": "Q",
"777": "R",
"7777": "S",
"8": "T",
"88": "U",
"888": "V",
"9": "W",
"99": "X",
"999": "Y",
"9999": "Z"
}

phone_charcters_encrypt = {
"A": "2",
"B": "22",
"C": "222",
"D": "3",
"E": "33",
"F": "333",
"G": "4",
"H": "44",
"I": "444",
"J": "5",
"K": "55",
"L": "555",
"M": "6",
"N": "66",
"O": "666",
"P": "7",
"Q": "77",
"R": "777",
"S": "7777",
"T": "8",
"U": "88",
"V": "888",
"W": "9",
"X": "99",
"Y": "999",
"Z": "9999",
}


# decrypt function 
def decrypt(message):
    decrypted = []


# Encrypt function
def encrypt(message):
    encrypted = []




# Greet the user
print("Hello, This is a phone chraracter cipher program")
name = input("Before we begin, what is your name? ")
print(f"Hello {name} lets get started")

def start_agian():
    # Ask if they want to decrypt or encrypt a message.
    choice = (input("Would you like to [d]ecrypt or [e]ncrypt a message? ").strip().lower())
    if choice != "d" or choice != "e":
            print("Invalid input. Please enter 'd' for decrypt or 'e' encrypt a message?")
            start_agian()
    while True: 
        # Decrypt the message
        if choice == "d":
            message = input("Enter the message you would like to decrypt: ")
            print(f"Decrypted message: {decrypt(message)}")

        # Encrypt the message
        elif choice == "e":
            message = input("Enter the message you would like to encrypt: ")
            print(f"Encrypted message: {encrypt(message)}")

        # Invalid choice
        else:
            print("Invalid choice, Please enter 'd' or 'e'. ")
            continue

    # Ask the user if thye want to decrypt or encrypt another message. If not write a goodbye message and exit the program
        while True:
            #Ask the user if they want to play again
                play_again = input("\nWould you like to decrypt or encrypt another message? [y/n] ").lower()
                if play_again == "n":
                    print("Thank you for using this website for your dinner invitation!")
                    exit()
                elif play_again == "y":
                    start_agian()
                else: 
                    print("Invalid choice, Please enter 'y' or 'n'. ")
                    continue
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


def start_agian():
    while True:
        # Ask if they want to decrypt or encrypt a message.
        choice = (input("Would you like to [d]ecrypt or [e]ncrypt a message? ").strip().lower())

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
        
        play_again = input("Would you like to encrypt or decrypt another message? (y/n): ").strip().lower()
        if play_again == "n":
            print("Thank you for using the Phone Character Cipher program. Goodbye!")
            break
        else: 
            print("Invalid choice, Please enter 'y' or 'n'. ")
            continue

# Greet the user
print("Hello, This is a phone chraracter cipher program")
name = input("Before we begin, what is your name? ")
print(f"Hello {name} lets get started")

start_agian()
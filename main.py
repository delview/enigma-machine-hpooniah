# Start Enigma Machine

# Phone charcters matching

phone_charcters_decrypt = {
"2": ["A", "B", "C"],
"3": ["D", "E", "F"],
"4": ["G", "H", "I"],
"5": ["J", "K", "L"],
"6": ["M", "N", "O"],
"7": ["P", "Q", "R", "S"],
"8": ["T", "U", "V"],
"9": ["W", "X", "Y", "Z"],
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
    choice = input("Would you like to [d]ecrypt or [e]ncrypt a message? ").strip().lower()

    # Decrypt the message
    while True: 
        if choice == "d":
            message = input("Enter the message you would like to decrypt: ")

        # Encrypt the message
        if choice == "e":
            message = input("Enter the message you would like to encrypt: ")

        # Invalid choice
        else:
            print("Invalid choice, Please enter 'd' or 'e'. ")

    # Print the decripted message 

    # Print the encrypted message

    # Ask the user if thye want to decrypt or encrypt another message. If not write a goodbye message and exit the program
        while True:
            #Ask the user if they want to play again
                play_again = input("\nWould you like to decrypt or encrypt another message? [y/n] ").lower()
                if play_again == "n":
                    print("Thank you for using this website for your dinner invitation!")
                    exit()
                elif play_again == "y":
                    start_agian()
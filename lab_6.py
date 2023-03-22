#  Sergio Acosta

def encode(string):
    encoded_password = ""
    for i in string:
        i = int(i)
        i += 3
        encoded_password += str(i)
    return encoded_password

def decode(encoded):
    decoded_encoded = ""
    for i in encoded:
        i = int(i)
        i -= 3
        decoded_encoded += str(i)
    return decoded_encoded

if __name__ == "__main__":
    while True:
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            string = input("Please enter your password to encode: ")
            encoded = encode(string)
            print("Your password has been encoded and stored!")
            print()
        elif option == 2:
            decoded_encoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded_encoded}")
        elif option == 3:
            break
        else:
            print("Incorrect selection! Please try again.")
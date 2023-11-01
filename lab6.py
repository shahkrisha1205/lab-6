def encode(password):
    convert = ""
    for i in range(len(password)):
        if str(password[i]) == "0":
            digit = "3"
        elif str(password[i]) == "1":
            digit = "4"
        elif str(password[i]) == "2":
            digit = "5"
        elif str(password[i]) == "3":
            digit = "6"
        elif str(password[i]) == "4":
            digit = "7"
        elif str(password[i]) == "5":
            digit = "8"
        elif str(password[i]) == "6":
            digit = "9"
        elif str(password[i]) == "7":
            digit = "0"
        elif str(password[i]) == "8":
            digit = "1"
        elif str(password[i]) == "9":
            digit = "2"
        convert += digit
    return convert

def decode():
    convert = ""
    for i in range(len(new_password)):
        if str(new_password[i]) == "0":
            digit = "7"
        elif str(new_password[i]) == "1":
            digit = "8"
        elif str(new_password[i]) == "2":
            digit = "9"
        elif str(new_password[i]) == "3":
            digit = "0"
        elif str(new_password[i]) == "4":
            digit = "1"
        elif str(new_password[i]) == "5":
            digit = "2"
        elif str(new_password[i]) == "6":
            digit = "3"
        elif str(new_password[i]) == "7":
            digit = "4"
        elif str(new_password[i]) == "8":
            digit = "5"
        elif str(new_password[i]) == "9":
            digit = "6"
        convert += digit
    return convert

value = True
def main():
    while value == True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            new_password = encode(password)
        elif option == 2:
            pass
        elif option == 3:
            break


if __name__ == "__main__":
    main()

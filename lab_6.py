def encode(password):
	result = ""
	for numbers in password:
		list = str((int(numbers) + 3) % 10)
		result += list
	return result

def decode(password):
	pass

def menu():
	print("Menu")
	print("-------------")
	print("1. Encode")
	print("2. Decode")
	print("3. Quit")

def main():
	test = True
	while test:
		menu()
		user_input = int(input("Please enter an option: ")
		if user_input == 1:
			passowrd = int(input("Please enter your password to encode: )
			print("Your password has been encoded and stored!")
		elif user_input == 2:
			pass
		else:
			test = False

if __name__ = "__main__":
	main()

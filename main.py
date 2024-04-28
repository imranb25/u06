import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_password_length():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Length must be a positive integer.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    length = get_password_length()
    password = generate_password(length)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()


import string
import random
import pyperclip

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_symbols=True, avoid_similar=False):
    if length < 4:
        print("Password length must be at least 4.")
        return None

    charset = ""
    if use_upper:
        charset += string.ascii_uppercase
    if use_lower:
        charset += string.ascii_lowercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += string.punctuation
    if not charset:
        print("Select at least one character type.")
        return None

    if avoid_similar:
        for c in "Il1O0":
            charset = charset.replace(c, "")

    password = ''.join(random.choice(charset) for _ in range(length))
    return password

def copy_password(password):
    pyperclip.copy(password)
    print("Password copied to clipboard!")

def save_password(password):
    if not password:
        print("Generate a password first.")
        return
    file_name = input("Enter the file name to save the password (e.g., password.txt): ")
    with open(file_name, "w") as f:
        f.write(password)
    print(f"Password saved to {file_name}")

def main():
    print("Welcome to the Command-Line Password Generator!")
    
    # Input parameters
    length = int(input("Enter password length (minimum 4): "))
    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
    use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == "y"
    use_digits = input("Include digits? (y/n): ").strip().lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"
    avoid_similar = input("Avoid similar characters (Il1O0)? (y/n): ").strip().lower() == "y"

    # Generate password
    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols, avoid_similar)
    
    if password:
        print(f"\nGenerated Password: {password}")
        
        # Option to copy password to clipboard
        copy_option = input("Do you want to copy the password to clipboard? (y/n): ").strip().lower()
        if copy_option == "y":
            copy_password(password)
        
        # Option to save password to file
        save_option = input("Do you want to save the password to a file? (y/n): ").strip().lower()
        if save_option == "y":
            save_password(password)
    else:
        print("Failed to generate password.")

if __name__ == "__main__":
    main()

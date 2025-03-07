import re 

# Check password strength
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: password length should be at least 8 characters"
    if not any(char.isdigit() for char in password):
        return "Weak: password should have at least one numeral"
    if not any(char.isupper() for char in password):
        return "Weak: password should have at least one uppercase letter"
    if not any(char.islower() for char in password):
        return "Weak: password should have at least one lowercase letter"
    if not any(char in ['$', '#', '@', '&', '%'] for char in password):
        return "Weak: password should have at least one of the symbols $, #, @, &, %"
    
    return "Strong: Your Password is Secure!"

# Function to check password strength
def password_strength():
    print("Welcome to the Password Strength Checker")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")
        if password.lower() == 'exit':  # Fixed method call
            print("Thank You for Using this Tool")
            break

        result = check_password_strength(password)
        print(result)

# Run the password checker tool
if __name__ == "__main__":  # Moved to correct indentation
    password_strength()

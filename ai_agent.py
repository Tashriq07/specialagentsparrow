import sys

# Hardcoded password
CORRECT_PASSWORD = "Rizqah$7"

def authenticate_user():
    """Authenticate the user by asking for a password."""
    attempts_remaining = 3
    while attempts_remaining > 0:
        entered_password = input("Enter your password: ")
        if entered_password == CORRECT_PASSWORD:
            print("Access granted!\n")
            return True
        else:
            attempts_remaining -= 1
            print(f"Incorrect password. {attempts_remaining} attempt(s) remaining.")
    
    print("Too many incorrect attempts. Exiting program.")
    sys.exit(1)

def main():
    """Main function for the AI Agent app."""
    print("AI Agent is starting...")
    
    # Authenticate the user
    authenticate_user()
    
    # Main functionality of the app
    print("Welcome to the AI Agent app!")
    print("You can now use the app's features.")
    # Add additional functionality here as needed

if __name__ == "__main__":
    main()
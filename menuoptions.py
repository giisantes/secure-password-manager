def add_password():
    print("\nAdd new password")

    site = input("Enter the site name: ").strip()
    if not site:
        print("Site is required. Please try again.")
        return
    
    email = input("Enter the email (optional): ").strip() or None
    username = input("Enter the username (optional): ").strip() or None

    password = input("Enter the password: ").strip()
    if not password:
        print("Password is required. Please try again.")
        return
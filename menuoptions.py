from database import insert_password, select_password_by_site
import auth

def add_password(cipher):
    
    print("\nAdd new password")
    
    site = input("\nEnter the site name: ").strip()
    if not site:
        print("Site is required. Please try again.")
        return
    email = input("Enter the email (optional): ").strip() or None
    username = input("Enter the username (optional): ").strip() or None

    password = input("Enter the password: ").strip()
    if not password:
        print("Password is required. Please try again.")
        return
    
    encrypted_password = cipher.encrypt(password.encode()).decode()
    insert_password(site, email, username, encrypted_password)
    print("Password added successfully.")

def view_passwords(cipher):

    print("\nView saved passwords")
    desired_site = input("Enter the name of the site you want to view passwords for: ").strip()
    if not desired_site:
        print("Site name is required. Please try again.")
        return
    login_details = select_password_by_site(desired_site)

    if not login_details:
        print(f"No passwords found for site: {desired_site}")
        return
    
    for site, email, username, encrypted_password in login_details:
        print(f"\nSite: {site}")
        if email:
            print(f"Email: {email}")
        if username:
            print(f"Username: {username}")
       #decrypt the password before displaying
        decrypted_password = cipher.decrypt(encrypted_password.encode()).decode()
        print(f"Password: {decrypted_password}")


       
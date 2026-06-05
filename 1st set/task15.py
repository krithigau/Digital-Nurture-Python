def login_user(username, password):
    if not username.strip() or not password.strip():
        print("Username and password cannot be blank.")
        return
    if username == "admin":
        if password == "A123":
            print("Login successful! Welcome, Krithiga.")
        else:
            print("Incorrect password.")
    else:
        print("Unknown username.")

user = "admin"
pwd = "A123"
login_user(user, pwd)
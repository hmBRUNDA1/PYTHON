import hashlib
user_db = {}
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def register(username, password):
    if username in user_db:
        print("Username already exists.")
    else:
        user_db[username] = hash_password(password)
        print("Created new user.")
def login(username, password):
    hashed = hash_password(password)
    if username in user_db and user_db[username] == hashed:
        print("Login Successful")
    else:
        print("Invalid username or password.")
register("john", "mypassword")     # Output: Created new user
login("john", "mypassword")        # Output: Login Successful
login("john", "wrongpassword")     # Output: Invalid username or password.
register("john", "newpassword")    # Output: Username already exists.

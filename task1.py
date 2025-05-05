# Initial user list
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

# Create: Add a new user
def add_user(users_list, user):
    users_list.append(user)

# Read: Retrieve user by ID
def get_user(users_list, user_id):
    for user in users_list:
        if user["id"] == user_id:
            return user
    return None

# Update: Update user info by ID
def update_user(users_list, user_id, new_data):
    for user in users_list:
        if user["id"] == user_id:
            user.update(new_data)
            return True
    return False

# Delete: Remove user by ID
def delete_user(users_list, user_id):
    for i, user in enumerate(users_list):
        if user["id"] == user_id:
            del users_list[i]
            return True
    return False

# Example usage:
print("Initial users:", users)

add_user(users, {"id": 3, "name": "Charlie", "email": "charlie@example.com"})
print("After adding Charlie:", users)

print("Get user with ID 2:", get_user(users, 2))

update_user(users, 1, {"name": "Alicia", "email": "alicia@example.com"})
print("After updating Alice:", users)

delete_user(users, 2)
print("After deleting Bob:", users)

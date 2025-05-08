users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]
def add_user(users_list, user):
    users_list.append(user)
def get_user(users_list, user_id):
    for user in users_list:
        if user["id"] == user_id:
            return user
    return None
def update_user(users_list, user_id, new_data):
    for user in users_list:
        if user["id"] == user_id:
            user.update(new_data)
            return True
    return False
def delete_user(users_list, user_id):
    for i, user in enumerate(users_list):
        if user["id"] == user_id:
            del users_list[i]
            return True
    return False
print("Initial users:", users)
add_user(users, {"id": 3, "name": "Charlie", "email": "charlie@example.com"})
print("After adding Charlie:", users)
print("Get user with ID 2:", get_user(users, 2))
update_user(users, 1, {"name": "Alicia", "email": "alicia@example.com"})
print("After updating Alice:", users)
delete_user(users, 2)
print("After deleting Bob:", users)

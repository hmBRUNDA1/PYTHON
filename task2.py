import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None

# Example usage:
print(is_valid_email("user@domain.com"))  # True
print(is_valid_email("user@domain"))      # False
print(is_valid_email("user.name@sub.domain.co"))  # True

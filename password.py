import random

def generate_password():
    goal_len = 0
    while goal_len < 8 or goal_len > 64:
        goal_len = int(input("Enter a password length between 8 and 64:"))
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*-_+=<>?"
    chars_len = len(chars)
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    while (has_digit==False or has_upper==False
           or has_lower==False or has_symbol==False):
        password = ""
        has_lower = False
        has_upper = False
        has_digit = False
        has_symbol = False
        while len(password) < goal_len:
            index = get_random(0, chars_len-1)
            char = chars[index]
            password += char
            if char.islower(): has_lower = True
            elif char.isupper(): has_upper = True
            elif char.isdigit(): has_digit = True
            else: has_symbol = True
    return password

def get_random(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)

print(generate_password())
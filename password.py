import random

# Convert a string into a number for use as random seed
def make_seed(s):
    seed = 1
    for c in s:
        # Convert each character to ASCI decimal number and multiply together
        seed *= ord(c)
    return seed


def get_random(lower_bound, upper_bound, keysmash, i):
    return random.randint(lower_bound, upper_bound)
    #num = seed*i

# main function: 
def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*-_+=<>?"
    chars_len = len(chars)
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False
    loops = 0 # How many characters have been generated across all attempts
              # Used for the second half of the random seed
    
    goal_len = 0
    while goal_len < 8 or goal_len > 64:
        goal_len = int(input("Enter a password length between 8 and 64:"))
    keysmash = ""
    # To make a random seed, have the user press arbitrary letters
    while len(keysmash) < 5:
        keysmash = input("Please enter a random keyboard smash of several letters:")
    seed = make_seed(keysmash)

    # Main loop: as long as the password lacks necessary characters,
    # keep trying to generate one.
    while (has_digit==False or has_upper==False
           or has_lower==False or has_symbol==False):
        password = ""
        has_lower = False
        has_upper = False
        has_digit = False
        has_symbol = False
        # Add characters to the password until it reaches the requested length.
        # Picks a random number as an index in the string of possible characters.
        while len(password) < goal_len:
            index = get_random(0, chars_len-1, keysmash, loops)
            char = chars[index]
            password += char
            # Check what kind of character was just added and update 
            # tracking variables.
            if char.islower(): has_lower = True
            elif char.isupper(): has_upper = True
            elif char.isdigit(): has_digit = True
            else: has_symbol = True
    # If the loop exits, then the password must have all necessary parts!
    return password


print(generate_password())
# Generate a random password of user-defined length, with randomization
# seeded from an arbitrary string entered by the user.

# Convert a string into a number for use as random seed
def make_seed(s):
    seed = 1
    # Loop through the string
    for i in range(len(s)):
        # Convert each character to ASCI decimal number and multiply together
        seed *= ord(s[i])
        # Bitwise XOR each 2 adjacent characters and add to seed
        if i % 2 == 1:
            seed += ord(s[i]) ^ ord(s[i-1])
    return seed


def get_random(lower_bound, upper_bound, seed, i):
    seed += i**3
    num = seed % (upper_bound - lower_bound + 1) + lower_bound
    return num


# main function: generate a random sequence of characters
def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*-_+=<>?"
    chars_len = len(chars)
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False
    loops = 0 # How many characters have been generated across all attempts
              # Used for the second half of the random seed, to make RNG result
              # vary from one character to the next.
    
    # Ask user how long a password to make, and keep asking if input is too 
    # small or large 
    goal_len = 0
    while goal_len < 8 or goal_len > 64:
        goal_len = int(input("Enter a password length between 8 and 64:"))
    
    # To make a random seed, have the user press arbitrary letters.
    # This is the first part of random seed, to make RNG results vary each time
    # the program is run.
    keysmash = ""
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
            index = get_random(0, chars_len-1, seed, loops)
            loops += 1
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
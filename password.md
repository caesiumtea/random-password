## requirements
https://twitter.com/codedex_io/status/1633156195472011278

Create a generate_password() function that generates a random strong password.
Password must contain:
- One number (0-9)
- One uppercase letter (A-Z)
- One lowercase letter (a-z)
- One special character (e.g., ! and _)

_Bonus challenge: avoid using any Python modules or packages._ This means writing a randomness function from scratch!

## plan
- First, write the function using the `random` module
- Then, add a helper function that implements my own randomness method
- Write it with the helper function from the start though, so that there's less to change later, but intially just treat it as a wrapper for the module
- Once the function works, go back to add exceptions for bad inputs

## reference 
### string methods/functions
- chr()
- .islower()
- .isupper()
- .isdigit()

### random
- the python random module uses an algorithm called the [Mersenne Twister](https://blogs.mathworks.com/cleve/2015/04/17/random-number-generator-mersenne-twister/) for its random generator

## pseudocode
### variables
- `pass` for holding the password we're making - empty string 
- `goal_len` to hold user input for password length
- `chars` string with all the availalbe characters
    - concat all characters we want to appear in paswords
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*-_+=<>?"
- `chars_len` length of available characters
- `has_upper `(starts false)
- `has_lower `(starts false)
- `has_digit `(starts false)
- `has_symbol` (starts false)

- `keysmash` for the user input random seed
- `attempts` will be used to modify the random seed, and must NOT be reset between loops

### functions

### generate_password()
- get user input to ask how long the password should be
    - validating that the input is an int between 8 and 64
- while (has_digit==False or has_upper==False or has_lower==False or has_symbol==False)
    - set pass="", has_ to false
    - loop as many times as length of password requested
        - loop condition: is `pass` at least as long as the length requested?
        - randomly pick a character from the set of (uppercase letters, lowercase letters, symbols, numbers)
            - pick a random number between 0 and length of concat string
            - chr(number) to convert it to ASCII character
            - increment `attempts`
        - add that char to `pass` - `pass + num`
        - check its type and set relevant variable to true
            - isdigit, islower, isupper 
            - if all 3 are false then it must be a symbol, so set has_symbol true
- if we're out of the loop, then it has everything needed, so return pass! (print pass)



### helper function: get_random()
- for first draft, this will just be a wrapper around the python random module
- params: keysmash, i,
          lower_bound, upper_bound - both inclusive, because that's how random.randint() works
          - if you wanted to be extra rigorous you could check that the bounds are in the right order, but here it's unneeded because lower is always gonna be 0
          - actually these could all just be globals idk
- something about user input? ask the user for a keysmash?
- at some point, use ord() on each char to convert the string to a number... maybe multiply the result by each char's ord in turn to make a real big number, don't worry about overflow though, that doesn't matter
- mash the result around based on a number that changes after every attempt to generate a random number
    - maybe first multiply by that number and then use the number to apply a bit shift or similar
    - why? because the random seed is the same! you don't want to ask the user for input for every single letter of the password, so you need another factor to differentiate the input between one function call and the next. the number of iterations is something that you can make sure will change every time.
- mod by `upper_bound - lower_bound + 1` then add `lower_bound`
    - you want the mod of the randint to have a number of different possible outcomes equal to the number of ints between the bounds (inclusively); you need to add 1 because the bounds are both inclusive and just like empirically, without adding 1, the number of possible outcomes would be 1 too small and you'd never hit the upper bound
    - e.g. get_random(3, 9)
      (rand % (9 - 3 + 1)) + 3
      (rand % 7) gives a result 0-6
      after adding 3, the range of results becomes 3-9, matching the bounds given




##############


# backup (unused ideas)

### helper function: compose_password()
- params: goal_len
- returns: password

### special characters to include: ASCII numbers
33, 35-38, 42-43, 45, 48-57, 60-90, 94-95, 97-122

- check if `pass` contains all necessary characters
    - does it have lowercase letter?
    - does it have uppercase letter?
    - does it have symbol?
    - does it have numeral?
- if it's missing something...
    - reset `pass` to ""
    - go to loop again
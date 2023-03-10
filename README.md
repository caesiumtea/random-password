# Random password generator

This is a submission for the [March Code Challenge](https://twitter.com/codedex_io/status/1633156195472011278) issued by [Codedex.io](https://www.codedex.io/). The challenge:

> In this month's challenge, you will design a Python program that generates strong passwords. 🐍
> Generally, a strong password consists of at least the following:
> - One number (0-9)
> - One uppercase letter (A-Z)
> - One lowercase letter (a-z)
> - One special character (e.g., ! and _)
> Create a generate_password() function that generates a random strong password.

I have also decided to take up the extra challenge of solving this without using any modules or packages! That means writing my own random number generator.

If you want to join the challenge too, you can submit your solution on the Twitter post linked above by March 21, 2023.

## Usage
**This was made as a learning exercise, not for practical use. You can still use it to generate passwords if you really want, it's better than using your dog's name, but don't count on it for true randomness.**

You can run the program on [repl.it](https://replit.com/@caesiumtea/Python-random-password-generator?v=1). First it will ask for a number between 8 and 64 (inclusive) for the length of the password. If you enter something other than an integer here, the program will crash. If you enter a number that's not between 8 and 64, it will just keep asking.

Next, enter any string of text--the intention is that you just randomly bang on your keyboard with your fists for a bit. It has to be at least 5 characters long, or else the program will keep asking. There is currently no upper bound on the length of this text, but beware that very long strings will increase computation time and maybe even crash the repl.it interpreter. 

The resulting password won't include or resemble the text entered; instead the text will be converted to numbers, which are then used to pick new letters.

## Development
If you're curious about my development process, you can see my pseudocode and development plan in [password.md](password.md), and this rough [flowchart](password_flowchart.jpg) of the basic algorithm for composing a password. Though actually, the flowchart only shows the loop for composing a single password--I didn't decide until after finishing this chart that I would put it all inside of another 

Unfortunately, I didn't make any diagrams or anything for my random number generation process, even though that's what probably needs more explanation.

The randomization is based on two factors: an arbitrary string typed in by the user, and the number of times the randomizer loop has run during the current execution. The user input is responsible for making the result different each time the program is run (as long as the input varies, that is--entering the same text will always result in the same password), and the number of loops is responsible for making the RNG result vary from character to character.

First, at the start of the program, the text input is converted to a number, using the `ord()` function to get the ASCII decimal representation of each character. These ASCII decimal values are all multiplied together. Then, it takes the bitwise XOR of every adjacent pair of these values, and adds those to the product from the last step. The purpose of this second step is to make the order of letters matter--without it, entering "abab" and "aabb" would give the same password. This all makes up the random seed that's unique to the input string, but is consistent through the course of one execution of the program.

For each iteration of the random generation loop, the random seed is modified slightly. This time is simpler: the "loops so far" value is cubed (to widen the variation between values) and then summed with the random seed. 

Then, for the RNG to give a result in the requested range, it grabs the sum from the last step and takes its modulo with respect to the number of possible outputs desired (AKA the difference between the upper and lower bounds, +1 to account for the upper bound being inclusive), and then adds the lower bound to it so that the range starts at the right place.

Finally, the random number is used as an index for a string of possible password characters, to choose a random character.

The idea to choose a pseudo-random result based on text input by the user comes from those "prediction" sites that used to be popular on Livejournal, where you'd type in your name and it would tell you which character you are or how you'll die or something like that (based, as far as I know, on some hash of the text input).

## Known issues
- The program will produce an error if the user enters a non-integer when asked for password length
- I haven't tested how the get_random helper function will behave if it's given an upper bound that's smaller than the lower bound, and there's currently no validation for this. This shouldn't ever be an issue when using the program as it's currently written, since the bounds are basically hard-coded into the one get_random call, but it could cause problems later if another get_random call was added, especially if it had input-based bounds.

## Note to Codedex challenge admin
If you end up considering this for the "special prize" (and if you're choosing the prize based on quality of the solution), please note that I am a more experienced user than many others on Codedex--I don't want to overshadow the amazing work of newer devs!

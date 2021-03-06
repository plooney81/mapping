# Letter histogram program that asks for user input, and prints a dictionary containing
# the tally of how many times each letter in the alphabet was used in the word

# lets first ask for the user input, while loop that will keep asking as long as user inputs a number, once inputs a string it will break
user_input = input('Please input a word you would like to see the letter histogram for:\n> ')

# lets convert everything to lower case first before we try and count the number of letters
user_input = user_input.lower()

# first we need our empty dictionary so we can add values
letter_hist = {}

#sort user input
user_input = sorted(user_input)

# for loop that iterates over our sorted string
for char in user_input:
    # so if the char is already a key in the dictionary, then it adds onto the value
    if char in letter_hist:
        letter_hist[char] += 1
    # if the key doesn't already exist, then it initializes that key value to 1
    else:
        letter_hist[char] = 1

print(letter_hist)
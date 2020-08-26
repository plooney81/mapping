# program that asks the user for a sentaence as its input, and prints a dictionary containing 
# the tally of how many times each word in the alphabet was used in teh text.

# prompt the user to input a sentence
print('\nPlease input a sentence you would like to run through the sentence word counter')

# while loop that checks to make sure the input is a string
while True:
    user_input = input('> ')
    try:
        int(user_input)
        print('Invalid input, please input a sentence')
    except ValueError:
        break

# go ahead and convert it to lower case
user_input = user_input.lower()

# counter var that counts the total times we have iterated over the string
counter = 0

# counter var that counts the number of characters since the last space or punctuation
numb_index_since = 0

# empty list to house our words list
words_list = []

# we need to grab each specific word in the sentence
for char in user_input:
    # finds the spaces
    if char == ' ' or char == ',' or char == '.' or char == '!' or char == '?':
        # if the slicing is punctuation, then we add onto our numb_index_since variable
        if user_input[numb_index_since: counter] == ' ' or user_input[numb_index_since: counter] == '!' or user_input[numb_index_since: counter] == ',' or user_input[numb_index_since: counter] == '' or user_input[numb_index_since: counter] == '?':
            numb_index_since = counter + 1
        # if the slicing isn't punctuation, then we goahead and append the slicing to the list
        else:
            words_list.append(user_input[numb_index_since : counter])
            numb_index_since = counter + 1 #because we don't want the punctation
    # if its the second to last character and there isn't any punctuation, it grabs the last word
    elif (counter + 1) >= len(user_input):
        words_list.append(user_input[numb_index_since : counter + 1])
        numb_index_since = counter + 1
    counter += 1

# print(words_list)

# create our words_histogram
hist = {}

# now we need to count the number of times each word appears in list and add them to a dictionary
for word in words_list:
    # if the word already exists in the histogram, then we add onto the value
    if word in hist:
        hist[word] += 1
    # if not, then we go ahead and initate the value to 1
    else:
        hist[word] = 1


# now we need to sort based off the one with the most occurrences
sorted_hist = {}

# bigest value list
values_in_order = []

# loop through and find the biggest value for each key
for key in hist:
        values_in_order.append(hist[key])

# sorts the values in reverse order
values_in_order.sort(reverse = True)

# shorten the values to only the top three
values_in_order = values_in_order[:3]


# need to append our dictionaries values to our sorted dictionary based off the sorted numbers in values_in_order list
for keys in hist:
    for numbers in values_in_order:
        if hist[keys] == numbers:
            sorted_hist[keys] = hist[keys]

# print the new histogram
print(sorted_hist)
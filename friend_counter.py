# given the dictionary below, write a function countFriends()
# that accepts a dictionary as an argument and returns a new dictionary that includes a new key friends_count:

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# friend counter function that has a single argument of some dictionary
def countFriends(some_dicitonary):
    # variable that counts how many friends
    # friend_counter = len(some_dicitonary["friends"])
    # for loop that iteratoes over the ramit['friends'] list, for each index, it adds one to our friends_counter variable
    # can also be achieved by the friend_counter = len(some_dictionary["friends"]), where no looping is necessary
    friend_counter = 0
    for friends in some_dicitonary['friends']:
        friend_counter += 1
    # create our new key of "friends_count" and save the length of friend_counter to it
    some_dicitonary["friends_count"] = friend_counter
    # return that dicitonary
    return some_dicitonary

# call the function and save the return dictionary back to our original dictionary name
ramit = countFriends(ramit)

# print the dictionary
print(f'\n\n{ramit}')
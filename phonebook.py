# Problem:  
    # give the following dictionary, representing a mappin from names to phone numbers
    # write code to do the following:
        # 1). Print Elizabeth's phone number
        # 2). Add an entry to the dictionary: Kareem's number is 938-489-1234
        # 3). Delete Alice's phone entry
        # 4). Change Bob's phone number to '968-345-2345'
        # 5). Print all the phone entries

# initialize the dictionary from the problem
phonebook_dict = {
    'Alice' : '703-493-1834',
    'Bob' : '857-384-1234',
    'Elizabeth' : '484-584-2923'
}

# initiate a counter variable
counter = 0

while counter < 5:
    # print Elizabeth's number
    if counter == 0:
        print(f'\nElizabeth\'s number is: {phonebook_dict["Elizabeth"]}')
    elif counter == 1: 
        # how you add a key and value to a dictionary
        phonebook_dict.update({'Kareem' : '938-489-1234'})
        # can also do
        # phonebook_dict['Kareem'] = "938-489-1234"
    elif counter == 2:
        # how you delete a key and value from a dictionary
        del phonebook_dict["Alice"]
        # can also do this
        # phonebook_dict.pop("Alice")
    elif counter == 3:
        # update a value for a specific key in a dictionary
        phonebook_dict["Bob"] = '968-345-2345'
    elif counter == 4:
        # iterate over the dictionary to print all of them out
        print('\nHere are all the values in the dictionary:')
        for key in phonebook_dict.keys():
            print(f'{key}: {phonebook_dict[key]}\n')
    counter += 1
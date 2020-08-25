# given the following dictionary:
    # 1). Write a python expression that gets the email address of Ramit
    # 2). gets the first of ramit's interests
    # 3). gets the email address of Jasmine
    # 4). ggets the second of Jan's two interests

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

# 1). gets email of Ramit
print(f'\n\nHere is Ramit\'s Email: {ramit["email"]}')

# 2). gets the first of Ramit's interests
print(f'\nHere is Ramit\'s first interest: {ramit["interests"][0]}')

# 3). gets the email address of Jasmine
print(f'\nHere is the email address of Jasmine: {ramit["friends"][0]["email"]}')

# 4). gets the second of Jan's two interests
print(f'\nHere is the second of Jan\'s two interests: {ramit["friends"][1]["interests"][1]}\n\n')

# how to get the same answers from above, through looping:

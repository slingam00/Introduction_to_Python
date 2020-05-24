myDictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}
# Keys are: 'a', 'b', 'c'
# Values are: 1, 2, 3

# Can get the value of a specific key in 2 ways

# First Way - Referring to key name
print(myDictionary['a'])  # returns 1

# Second Way - Using the get method
print(myDictionary.get('c'))  # returns 3

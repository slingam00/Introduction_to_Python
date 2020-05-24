mySet = {'a', 'b', 'c'}

# Adding to the set
mySet.add('d')
print(mySet)  # Sets are unordered so the resulting Set varies
              # An example of a result would be {'a', 'd', 'b', 'c'}

# Removing from the set
mySet.remove('c')

# Updating the set
mySet.update(['e', 'f', 'g']) # Result could look something like: {'a', 'e', 'b', 'f', 'g'}

def hello():
    return("Hello")

print(hello())     # printing the call of the function which returns "Hello"
                 

def name(firstName, lastName):
    return("Hello, my name is " + firstName + " " + lastName)

print(name("John", "Doe"))   # name function gets called
                             # firstName getting passed in is 'John'
                             # lastName getting passed in is 'Doe'
                             # The result is the String: Hello, my name is John Doe

# class Person:
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender

# def greet(person):
#     print('hi',person.name,'I am a', person.gender)

# p = Person('pratik', 'male')
# greet(p)


class Person:                  # Class

    def __init__(self, name, gender):   # Constructor
        self.name = name                # Instance attribute
        self.gender = gender  
    def __str__(self):
        return f'Name:{self.name},Gender:{self.gender}'          # Instance attribute

# def greet(person):              # Normal function
#     person.name = "ankit"

p = Person("nitish","male")     # Object (Instance)

p.name                          # Attribute

p.gender                        # Attribute
    

print(p)
# Create a method to print that the person can drive
class Adult :

    def __init__(self, name, age, eye_col, hair_col) :
        self.name = name
        self.age = age
        self.eye_col = eye_col
        self.hair_col = hair_col
    
    def can_drive(self) :
        print(f"{self.name} can drive")

# Create a method to print that the person cannot drive
# This inherits all of the data from the adult class so we don't need to declare anything or have an init
class Child(Adult) :
       def can_drive(self) :
            print(f"{self.name} cannot drive")

while True :
    name = input("Please enter your name\n")
    hair = input("Please enter your hair color\n")
    eye = input("Please enter your eye color\n")
    print("Please enter you age") 
    while True :
        age = input()
        try :
            int(age)
            break
        except :
            print("Invalid input, please try again")

    if int(age) >= 18 :
        person = Adult(name, age, eye, hair)
    else :
        person = Child(name, age, eye, hair)

    person.can_drive()
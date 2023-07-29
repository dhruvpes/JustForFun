class SpecialString:

    def __len__(self):
        return 42
    
obj1 = SpecialString()
# print(len(obj1))
#############################
class Bird:
    
    def fly(self):
        print("I fly with wings")

class Airplane:

    def fly(self):
        print("Flying with fuel")
    
class Fish:

    def swim(self):
        print("Fishes swim in the sea")

    def fly(self):
       print("Sorry, invalid choice!! I cannot fly")
b1 = Bird()
# print(b1.fly)
# print(b1.fly())

# Illustration of Duck typing

for obj in Bird(), Airplane(), Fish():
    obj.fly()

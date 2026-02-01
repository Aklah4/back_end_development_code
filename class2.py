class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return (f"my name is {self.name}, i am {self.age}, years old")    
    

person = student("Emmanuel", 29)   
print(person.introduce()) 
# Clases

class persona: 
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def walk(self):
        print(f"{my_person.name} esta caminando")


my_person = persona("andreslo", "gonzalez")

print(f"{my_person.name} {my_person.surname}")
my_person.walk()
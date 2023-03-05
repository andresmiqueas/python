# Bucles / Loops / Ciclos

# While -- Mientras

"""
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1

while my_condition < 20:
    my_condition += 1
    print(my_condition)
    if my_condition == 15:
        break
"""

# For -- Para

my_list = (35, 30, 27, 18, 55, 40)
my_tuple = ("Andres", "Miqueas", "Gonzalez")
my_dict = {
    "Nombre":"Andrelo", 
    "Apellido":"Gonzalez", 
    "Edad":27,
    "Lenguajes":{"Python", "JavaScript", "C"},
    1:{"Amarillo", "Verde"},
    "Estatura":1.79
}

for elements in my_list:
    print(elements)
    if elements == 30:
        print("se para")
        break


# Diccionarios // Relacion clave - valor

my_dict = dict()

my_other_dict = {"Nombre":"Andrelo", "Apellido":"Gonzalez", "Edad":27, 1:"Python"}

my_dict = {
    "Nombre":"Andrelo", 
    "Apellido":"Gonzalez", 
    "Edad":27,
    "Lenguajes":{"Python", "JavaScript", "C"},
    1:{"Amarillo", "Verde"},
    "Estatura":1.79
}

my_dict ["Calle"] = "Brandsen"

print("Nombre" in my_dict)
print(my_dict["Edad"]) 

my_list=["Nombre", 1, "Piso"]

my_mew_dict = dict.fromkeys((my_list))
print(my_mew_dict)
my_mew_dict = dict.fromkeys(my_dict, ("Andres", "Gonzalez"))
print(my_mew_dict)

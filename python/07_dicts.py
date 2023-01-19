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


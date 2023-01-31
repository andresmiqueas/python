# Excepciones -- manejo de errores


numer_one = 5
number_two = "1"


try: # si hay un try hay un except
    print(numer_one + number_two)
    print("No se ha producido un error")
except:
    # se ejecuta si se produce un error
    print("Se ha producido un error")
else: # opcional
    # se ejecuta si NO se encuentra un error
    print("La ejecucion contunua")
finally: # opcional
    # se ejecuta siempre
    print("Linea final")




try:
    print(numer_one + number_two)
    print("No se ha producido un error")
except TypeError as error:
    # si se produce un error de tipo Type, lo capturo y lo muestro en consola
    print(error)




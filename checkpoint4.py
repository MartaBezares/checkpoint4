import math
from decimal import Decimal
#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
#lista
alumnos = ["Marta", "David", "Sara", "Raul"]
#tupla
saga_novelas = ("Una dama en apuros", "Una dama prometida", "Un dama inesperada")
#float
precio = 83.58
#int
cantidad = 5
#decimal
precio_cantidad = precio * cantidad
print(Decimal(precio_cantidad))
#diccionario
cantantes = {
  "pop": "Michael Jackson",
  "rock": "Elvis Presley",
  "jazz": "Ella Fitzgerald"
}
print()

#Exercise 2: Round your float up.
print(math.ceil(precio))
print()

#Exercise 3: Get the square root of your float.
print(math.sqrt(precio))
print()

#Exercise 4: Select the first element from your dictionary.
cantante_pop = cantantes["pop"]
print(cantante_pop)
print()

#Exercise 5: Select the second element from your tuple.
print(saga_novelas[1])
print()

#Exercise 6: Add an element to the end of your list.
alumnos.append("Berta")
print(alumnos)
print()

#Exercise 7: Replace the first element in your list.
alumnos[0] = "Mario"
print(alumnos)
print()

#Exercise 8: Sort your list alphabetically.
alumnos.sort()
print(alumnos)
print()

#Exercise 9: Use reassignment to add an element to your tuple.
saga_novelas += ("Una dama decidida", )
print(saga_novelas)

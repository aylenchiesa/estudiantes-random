import random

estudiantes = [
    "x"
]

random.shuffle(estudiantes)

grupo1 = estudiantes[:18]
grupo2 = estudiantes[18:35]

print("Grupo 1: ")
for i in grupo1:
    print("-", i)
print()
print("Grupo 2: ")
for i in grupo2:
    print("-", i)


import random

estudiantes = [
    "Abelenda Ana Paula", "Alcaràz Pikarski Nicolás Agustìn", "Arostegui Simón", "Asuad Manuel", "Azcona Matilda Lorena",
    "Benitez Juan Pablo", "Bladilo Victoria", "Britez Ignacio Tobias", "Cáceres Pared Marcelo Agustín", "Caminos Roberto Damian",
    "Codermatz Juan Valentino", "Codutti Laura Agostina", "Correa Aylen", "Agostina", "Costantini Matias Emanuel",
    "Diez Noelia Tatiana", "Galvez Juan", "Gauto Rosario", "Gomez Jeronimo Adolfo Javier", "Invaldi Juan Martin",
    "Kaposvari Franco", "Karatanasopuloz Julian", "Lopez Lecube Lautaro", "Maidana Lautaro Nahuel", "Meza Chiesa Aylen Giovana",
    "Meza Santiago Exequiel", "Mordka Lucas Ayén", "Mortola Jorge Homero", "Mortola Santino", "Pzocik Erwin Nahum",
    "Quetglas Agustin", "Repka Soto Máximo", "Romero Stach Lautaro", "Segovia Juan Tomas", "Sosa Wilka Francisco Raul",
    "Soto Juan Bautista"
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

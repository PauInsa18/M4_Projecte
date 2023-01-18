areas = [ "cuina", 7.88, "menjador", 13.0, "terrassa", 20.34, "lavabo", 6.55, "habitació1", 7.98, "habitació2", 12, "rebedor", 4.23]

#Imprimir el segundo elemento
print(areas[1])

#Imprimir el ultimo elemento
print(areas[13])

#Imprimir l'area de la terrasa
print(areas[5])

#Imprimir del primer element al tercer element
print(areas[0:3])

#Imprimir del tercer element a l’últim
print(areas[3:0])

#Imprimir el total de l'àrea de les dues habitacions
print(areas[9] + areas[11])

#Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
areas.append("Pati Interiro")
print(areas)
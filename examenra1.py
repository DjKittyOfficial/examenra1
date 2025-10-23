PRECIO_DECIMO = 20
NUMEROS_BOMBO = 100000

print("**** Lotería de Navidad ****")

nombre = input("Bienvenido. ¿Cuál es tu nombre? ")

inversion = float(input("Perfecto " + nombre + ". Indícame la cantidad invertida (€): "))

numeros_comprados = inversion / PRECIO_DECIMO 
probabilidad = (numeros_comprados / NUMEROS_BOMBO) * 100

print("La probabilidad de ganar el gordo es", probabilidad, "%")

inversion_1 = PRECIO_DECIMO * NUMEROS_BOMBO * (1 / 100)
inversion_5 = PRECIO_DECIMO * NUMEROS_BOMBO * (5 / 100)
inversion_10 = PRECIO_DECIMO * NUMEROS_BOMBO * (10 / 100)

print("Quieres más posibilidades de ganar?")
print("Para tener un 1% necesitas invertir", inversion_1, "€")
print("Para tener un 5% necesitas invertir", inversion_5, "€")
print("Para tener un 10% necesitas invertir", inversion_10, "€")


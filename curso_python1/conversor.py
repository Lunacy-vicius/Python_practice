def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos +  " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "  dolares")

menu = """ 
Bienvenido al conversor de monedas 😜

1 - Pesos mexicanos
2 - Pesos argentinos
3 - Pesos colombianos
Elige una opción"""
opcion = int(input(menu))



if opcion == 1:
    conversor("mexicanos", 20)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("colombianos", 3875)
else:
    print("ingresa una opción correcta")


#pesos = input("¿Cuantos pesos mexicanos tienes?: ")
#pesos = float(pesos)
#valor_dolar = 20
#dolares = pesos / valor_dolar
#dolares = round(dolares, 2)
#dolares = str(dolares)
#print("Tienes $" + dolares + "  dolares")

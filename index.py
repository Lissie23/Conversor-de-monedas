usd = [20.28, 0.95]
mxn = [0.049, 0.047]  
eur = [1.05, 21.28] 

# usd[0] para convertir de usd a mxn
# usd[1] para convertir de usd a eur
# mxn[0] para convertir de mxn a eur
# mxn[1] para convertir de mxn a usd
# eur[0] para convertir de eur a usd
# eur[1] para convertir de eur a mxc

#Mostrar al usuario el menu
def showMenu(): 
    print("Bienvenido a tu conversor de moneda")
    print("1. Convertir moneda")
    print("2. Ver tasas de cambio")
    print("3. Actualizar tasas")
    print("4. Salir")

#Permitir al usuario seleccionar la moneda de origen y destino (USD, EUR, MXN)
def convertCurrency():  
    origen = input("Ingresa la moneda de origen (USD, MXN, EUR): ").upper()
    destino = input("Ingresa la moneda de destino (USD, MXN, EUR): ").upper()

    if origen == destino:
        print("Las monedas son iguales. No es necesaria la conversión.")
        return
    
    try:
        cantidad = float(input("Ingresa la cantidad a convertir: "))
    except ValueError:
        print("Error: Ingresa un número válido.")
        return
    
    #Operaciones para el cambio de moneda
    if origen == "USD" and destino == "MXN": 
        resultado = cantidad * usd[0]
        print(cantidad, origen, "equivale a",resultado, destino)
        
    elif origen == "USD" and destino == "EUR":
        resultado = cantidad * usd[1]
        print(cantidad, origen, "equivale a", resultado, destino)

    elif origen == "MXN" and destino == "EUR":
        resultado = cantidad * mxn[0]
        print(cantidad, origen, "equivale a", resultado, destino)

    elif origen == "MXN" and destino == "USD":
        resultado = cantidad * mxn[1]
        print(cantidad, origen, "equivale a", resultado, destino)
    
    elif origen == "EUR" and destino == "USD":
        resultado = cantidad * eur[0]
        print(cantidad, origen, "equivale a", resultado, destino)

    elif origen == "EUR" and destino == "MXN":
        resultado = cantidad * eur[1]
        print(cantidad, origen, "equivale a", resultado, destino)

    else:
        print("Conversión no disponible")


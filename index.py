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

#Mostrar las tasas de cambio al usuario
def showExchangeCurrency(): 
    print("Tasas de cambio actuales")
    print("USD =", usd[0], "MXN")
    print("USD =", usd[1], "EUR")
    print("MXN =", mxn[0], "EUR")
    print("MXN =", mxn[1], "USD")
    print("EUR =", eur[0], "USD")
    print("EUR =", eur[1], "MXN")

#Actualizar las tasas de cambio
def updateExchangeCurrency(): 
    origen = input("Ingresa la moneda de origen (USD, MXN, EUR):").upper()
    destino = input("Ingresa la moneda de destino (USD, MXN, EUR):").upper()
    
    try:
        nuevaTasa = float(input("Ingresa la nueva tasa: "))
    except ValueError:
        print("Error: Ingresa un número válido.")
        return

    if origen == "USD" and destino == "MXN":
        usd[0] = nuevaTasa
        print("Tasa actualizada: de USD a MXN =", usd[0])

    elif origen == "USD" and destino == "EUR":
        usd[1] = nuevaTasa
        print("Tasa actualizada: de USD a MXN =", usd[1])

    elif origen == "MXN" and destino == "EUR":
        mxn[0] = nuevaTasa
        print("Tasa actualizada: de MXN a EUR =", mxn[0])

    elif origen == "MXN" and destino == "USD":
        mxn[1] = nuevaTasa
        print("Tasa actualizada: de USD a MXN =", mxn[1])
    
    elif origen == "EUR" and destino == "USD":
        eur[0] = nuevaTasa
        print("Tasa actualizada: de USD a MXN =", eur[0])

    elif origen == "EUR" and destino == "MXN":
        eur[1] = nuevaTasa
        print("Tasa actualizada: de USD a MXN =", eur[1])

    else:
        print("Par de monedas no válido")
        return



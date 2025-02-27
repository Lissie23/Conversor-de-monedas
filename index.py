usd = [20.28, 0.95]
mxn = [0.049, 0.047]  
eur = [1.05, 21.28] 

# usd[0] para convertir de usd a mxn
# usd[1] para convertir de usd a eur
# mxn[0] para convertir de mxn a eur
# mxn[1] para convertir de mxn a usd
# eur[0] para convertir de eur a usd
# eur[1] para convertir de eur a mxn

# Mostrar al usuario el menú
def showMenu(): 
    print("\n🌍💰 Bienvenido a tu conversor de moneda 💰🌍")
    print("1️.Convertir moneda")
    print("2️. Ver tasas de cambio")
    print("3️. Actualizar tasas")
    print("4️. Salir")

# Permitir al usuario seleccionar la moneda de origen y destino (USD, EUR, MXN)
def convertCurrency():  
    origen = input("💱 Ingresa la moneda de origen (USD, MXN, EUR): ").upper()
    destino = input("💲 Ingresa la moneda de destino (USD, MXN, EUR): ").upper()

    if origen == destino:
        print("⚠️ Las monedas son iguales. No es necesaria la conversión.")
        return
    
    try:
        cantidad = float(input("💰 Ingresa la cantidad a convertir: "))
    except ValueError:
        print("❌ Error: Ingresa un número válido.")
        return
    
    # Operaciones para el cambio de moneda
    if origen == "USD" and destino == "MXN": 
        resultado = cantidad * usd[0]
    elif origen == "USD" and destino == "EUR":
        resultado = cantidad * usd[1]
    elif origen == "MXN" and destino == "EUR":
        resultado = cantidad * mxn[0]
    elif origen == "MXN" and destino == "USD":
        resultado = cantidad * mxn[1]
    elif origen == "EUR" and destino == "USD":
        resultado = cantidad * eur[0]
    elif origen == "EUR" and destino == "MXN":
        resultado = cantidad * eur[1]
    else:
        print("❌ Conversión no disponible")
        return
    
    print(f"✅ {cantidad} {origen} equivale a {resultado:.2f} {destino}.")

# Mostrar las tasas de cambio al usuario
def showExchangeCurrency(): 
    print("\n📊 Tasas de cambio actuales:")
    print(f"💵 USD = {usd[0]} MXN")
    print(f"💵 USD = {usd[1]} EUR")
    print(f"💵 MXN = {mxn[0]} EUR")
    print(f"💵 MXN = {mxn[1]} USD")
    print(f"💵 EUR = {eur[0]} USD")
    print(f"💵 EUR = {eur[1]} MXN")

# Actualizar las tasas de cambio
def updateExchangeCurrency(): 
    origen = input("✍️ Ingresa la moneda de origen (USD, MXN, EUR): ").upper()
    destino = input("✍️ Ingresa la moneda de destino (USD, MXN, EUR): ").upper()
    
    try:
        nuevaTasa = float(input("🔄 Ingresa la nueva tasa: "))
    except ValueError:
        print("❌ Error: Ingresa un número válido.")
        return

    if origen == "USD" and destino == "MXN":
        usd[0] = nuevaTasa
    elif origen == "USD" and destino == "EUR":
        usd[1] = nuevaTasa
    elif origen == "MXN" and destino == "EUR":
        mxn[0] = nuevaTasa
    elif origen == "MXN" and destino == "USD":
        mxn[1] = nuevaTasa
    elif origen == "EUR" and destino == "USD":
        eur[0] = nuevaTasa
    elif origen == "EUR" and destino == "MXN":
        eur[1] = nuevaTasa
    else:
        print("❌ Par de monedas no válido")
        return
    
    print(f"✅ Tasa actualizada: de {origen} a {destino} = {nuevaTasa}")

while True:
    showMenu()
    opcionElegida = input("🔹 Seleccione la opción que desea ejecutar: ")

    if opcionElegida == "1":
        convertCurrency()
    elif opcionElegida == "2":
        showExchangeCurrency()
    elif opcionElegida == "3":
        updateExchangeCurrency()
    elif opcionElegida == "4":
        print("👋 Gracias por usar el conversor de monedas. ¡Hasta luego!")
        break
    else:
        print("❌ Opción no válida. Intenta de nuevo.")


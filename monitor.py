import requests

def suite_hispanica_completa():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    # Configuración de todas las monedas hispanas
    # Formato: "Código": "País/Moneda"
    paises = {
        # Norte y Centroamérica
        "1": ("MXN", "México (Peso)"),
        "2": ("GTQ", "Guatemala (Quetzal)"),
        "3": ("HNL", "Honduras (Lempira)"),
        "4": ("NIO", "Nicaragua (Córdoba)"),
        "5": ("CRC", "Costa Rica (Colón)"),
        "6": ("PAB", "Panamá (Balboa)"),
        # El Caribe
        "7": ("CUP", "Cuba (Peso)"),
        "8": ("DOP", "Rep. Dominicana (Peso)"),
        # Sudamérica
        "9": ("COP", "Colombia (Peso)"),
        "10": ("VES", "Venezuela (Bolívar)"),
        "11": ("PEN", "Perú (Sol)"),
        "12": ("BOB", "Bolivia (Boliviano)"),
        "13": ("CLP", "Chile (Peso)"),
        "14": ("ARS", "Argentina (Peso)"),
        "15": ("PYG", "Paraguay (Guaraní)"),
        "16": ("UYU", "Uruguay (Peso)"),
        # Europa
        "17": ("EUR", "España (Euro)")
    }

    tasas_online = {}
    online = False

    try:
        print("🌍 Conectando con los mercados de la región...")
        respuesta = requests.get(url, timeout=5)
        tasas_online = respuesta.json()["rates"]
        online = True
    except:
        print("⚠️ Conexión lenta. Algunas tasas podrían requerir entrada manual.")

    print("\n" + "═"*55)
    print("   CONVERSOR PANHISPÁNICO | LEONEL GOLIAT   ")
    print("═"*55)

    # Imprimir el menú en dos columnas para que no sea tan largo
    items = list(paises.items())
    for i in range(0, len(items), 2):
        # Columna 1
        opt1, info1 = items[i]
        t1 = tasas_online.get(info1[0], 0)
        st1 = f"{t1:>8,.2f}" if t1 > 0 else "  Manual"
        linea = f"{opt1:>2}. {info1[1].ljust(22)} | {st1}"
        
        # Columna 2 (si existe)
        if i + 1 < len(items):
            opt2, info2 = items[i+1]
            t2 = tasas_online.get(info2[0], 0)
            st2 = f"{t2:>8,.2f}" if t2 > 0 else "  Manual"
            linea += f"  ||  {opt2:>2}. {info2[1].ljust(22)} | {st2}"
        
        print(linea)

    print("-" * 55)
    sel = input("Selecciona el número de moneda (1-17): ")

    if sel in paises:
        codigo, nombre = paises[sel]
        tasa_usar = tasas_online.get(codigo, 0)

        if tasa_usar <= 0:
            print(f"\n[!] Tasa de {codigo} no detectada automáticamente.")
            tasa_usar = float(input(f"👉 Ingresa tasa manual (1 USD = ? {codigo}): "))
        
        monto = float(input(f"\n¿Cuántos {nombre} tienes?: "))
        resultado = monto / tasa_usar
        
        print("\n" + "─"*45)
        print(f"💰 RESULTADO DE CONVERSIÓN:")
        print(f"{monto:,.2f} {codigo} ➔ ${resultado:,.2f} USD")
        print("─"*45 + "\n")
    else:
        print("❌ Selección fuera de rango.")

if __name__ == "__main__":
    suite_hispanica_completa()
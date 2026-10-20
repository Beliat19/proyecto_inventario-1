import asyncio
import time

async def verificar_inventario(item, precio):
    print(f"Buscando {item} en la bodega...")
    await asyncio.sleep(1)
    print(f"{item} encontrado. Precio: {precio:,}")
    return precio

async def procesar_pago(monto, placa):
    print(f"Procesando pago de {monto:,} para el vehículo {placa} con bre-b...")
    await asyncio.sleep(2)
    print(f"Pago aprobado para la placa {placa}.")
    return f"{placa}"

async def generar_factura(item, transaccion, placa):
    print(f"Generando factura para {item} (Placa: {placa}, REF: {transaccion})")
    await asyncio.sleep(1)
    print(f"Factura electrónica enviada para el vehículo {placa}")

async def atender_cliente(nombre, item, precio, placa):
    print(f"--- INICIO ATENCION AL CLIENTE ({nombre}) ---")
    
    precio_inventario = await verificar_inventario(item, precio)
    transaccion = await procesar_pago(precio_inventario, placa)
    await generar_factura(item, transaccion, placa)
    
    print(f"--- FIN ATENCION AL CLIENTE ({nombre}) ---")

    #-------------------------------------------

async def main():
    inicio = time.time()

    atencion = [
        atender_cliente("Cliente 1", "motor de Gixxer", 120000, "ABC-12F"),
        atender_cliente("Cliente 2", "filtro de aire", 45000, "XYZ-78H"),
        atender_cliente("Cliente 3", "pastillas de freno", 180000, "WOF-44D")
    ]

    await asyncio.gather(*atencion)
    fin = time.time()
    print(f"Tiempo total de ejecución: {fin - inicio:.1f} segundos")

asyncio.run(main())

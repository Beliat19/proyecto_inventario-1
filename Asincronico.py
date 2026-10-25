import random
import asyncio
import time

async def descargar_factura(numero_factura):
   
    print(f"[{time.strftime('%X')}] Iniciando descarga de la factura {numero_factura}....")
    await asyncio.sleep(random.randint(1, 3))

    print(f"[{time.strftime('%X')}] Factura {numero_factura} descargada con Exito.") 
    return f"Factura {numero_factura}"

async def main():
    print("--- INICIO DEL PROGRAMA ASINCRONICO ---")
    inicio = time.time()
    tareas = [
        descargar_factura(1),
        descargar_factura(2), 
        descargar_factura(3),
        descargar_factura(4),
        descargar_factura(5),

    ]

    await asyncio.gather(*tareas)

    fin = time.time()
    print(f"--- FIN DEL PROGRAMA ---")
    print(f"tiempo total: {fin - inicio:.1f} segundos")

asyncio.run(main())
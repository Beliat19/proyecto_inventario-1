import asyncio
import time



async def procesar_orden(repuesto):
    print(f"[{time.strftime('%X')}] iniciando orden de servicio para:  {repuesto}")

    disponible = await consultar_proveedor(repuesto)

    if disponible:
        print(f"[{time.strftime('%X')}] orden confirmada para:  {repuesto}")

    else
        print(f"[{time.strftime('%X')}] no hay stock para:  {repuesto}")


        

async def consultar_proveedor(repuesto):
    print(f"[{time.strftime('%X')}] contactando con el proveedor para:  {repuesto}")

    #tiempo de espera
    await asyncio.sleep(2) #llamada a una API, el envio al frontend (simulado)
    print(f"[{time.strftime('%X')}] proveedor respondio para:  {repuesto}")
    return true

    #punto de entrega
    asyncio.run(procesar_orden("kit de arrastre"))
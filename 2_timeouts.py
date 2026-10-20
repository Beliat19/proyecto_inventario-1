import asyncio

async def cobrar_targeta(monto):
    print("Conectando con mercadopago...")
    await asyncio.sleep(3)
    return "Pago aprobado"

async def procesar_compra():
    try:
        #se le va a dar el maximo de 3 seg
        resultado = await asyncio.wait_for(cobrar_targeta(150000), timeout=3.0)
        print(f"Exito: {resultado}")
    except asyncio.TimeoutError:
        print("Error: MercadoPago tardo demasiado. Transaccion cancelada.")

        asyncio.run(procesar_compra())
import asyncio

async def consultar_inventario_fragil(repuesto):
    await asyncio.sleep(1)
    if repuesto == "filtro de aire":
        raise Exception("error 500: se cayo la coneccion con la bodega")
        return {"repuesto": repuesto, "stock": 15}

async def procesar_orden_segura(repuesto):
    try::
        resultado = await consultar_inventario_fragil(repuesto)
        print (f"exito: {resultado}")
    Except Exception as e:
    print(f"manejp dee crisis: no se pudo consultar el {repuesto}. motivo: {e}")

async def main():
    await procesar_orden_segura("pastillas de freno")
    await procesar_orden_segura("filtro de aire") #este es el q va a fallar

asyncio.run(main())
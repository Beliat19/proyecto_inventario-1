import asyncio
import uuid

from database import (crear_producto,eliminar_producto,tareas_alerta,vender_producto,)


async def procesar_venta(codigo, cantidad_vendida):
    try:
        producto = await vender_producto(codigo, cantidad_vendida)
        print(
            f"Venta exitosa: {producto['nombre']}; "
            f"stock restante: {producto['stock']}."
        )
        return producto
    except ValueError as error:
        print(f"Venta rechazada por stock insuficiente: {error}")
        return None
    except KeyError as error:
        print(f"No se pudo completar la venta: {error}")
        return None


async def prueba_de_ventas():
    prefijo = uuid.uuid4().hex[:8]
    productos = [
        {
            "codigo": f"SIM-{prefijo}-1",
            "nombre": "Venta normal",
            "stock": 10,
            "cantidad": 3,
        },
        {
            "codigo": f"SIM-{prefijo}-2",
            "nombre": "Stock crítico",
            "stock": 5,
            "cantidad": 4,
        },
        {
            "codigo": f"SIM-{prefijo}-3",
            "nombre": "Venta sin existencias suficientes",
            "stock": 3,
            "cantidad": 4,
        },
        {
            "codigo": f"SIM-{prefijo}-4",
            "nombre": "Segunda venta normal",
            "stock": 12,
            "cantidad": 2,
        },
    ]

    await asyncio.gather(
        *(
            crear_producto(producto["codigo"], producto["nombre"], producto["stock"])
            for producto in productos
        )
    )

    try:
        resultados = await asyncio.gather(
            *(
                procesar_venta(producto["codigo"], producto["cantidad"])
                for producto in productos
            )
        )
        print(
            f"\nSimulación terminada: "
            f"{sum(resultado is not None for resultado in resultados)} "
            "ventas exitosas de 4 intentos."
        )
    finally:
        try:
            if tareas_alerta:
                await asyncio.gather(*tuple(tareas_alerta))
        finally:
            await asyncio.gather(
                *(eliminar_producto(producto["codigo"]) for producto in productos)
            )


if __name__ == "__main__":
    asyncio.run(prueba_de_ventas())

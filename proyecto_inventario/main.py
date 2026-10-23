# from fastapi import FastAPI, HTTPException, Request #importo mi framework
# from database import leer_base_datos, obtener_producto, guardar_base_datos
# from schemas import ProductoCreate
# import json-

# # Inicializar la aplicación
# app = FastAPI(
#     title="API inventarios SENA",
#     description="Mi primera API asíncrona",
#     version="1.0.0"
# )

# def cargar_inventario():
#     with open("inventario.json", "r", encoding="utf-8") as archivo:
#         return json.load(archivo)

# # Nuestro primer endpoint
# @app.get("/") # Decorador -> Función que recibe como parámetro otra función
# async def ruta_principal():
#     return {"mensaje": "¡Bienvenido a mi primera API Rest!"}

# @app.get("/estado")
# async def estado_servidor():
#     return {"status": "En línea", "servicios": "Operativos sin ningun invonveniente"}

# @app.get("/productos")
# async def listar_productos():
#     datos = await leer_base_datos()
#     return {"cantidad": len(datos), "productos": datos}

# @app.get("/productos/{codigo_producto}")
# async def buscar_un_producto(codigo_producto: str):
#     try:
#         # Para llamar a la función de obtener producto
#         producto = await obtener_producto(codigo_producto)
#         return producto
#     except KeyError:
#         raise HTTPException(status_code=404, detail="El producto soliciato no existe en la BD.")

#     #--------------------------------------------------------------------------------------------------------------------------------------------

# @app.get("/categorias")
# def obtener_categorias():
#     inventario = cargar_inventario()
#     categorias = set()
#     for producto in inventario:
#         categorias.add(producto["categoria"])
#     return list(categorias)

# #------------------------------------------------------------------------------------------------------------------------------------------------
# @app.get("/alertas/stock")

# def obtener_stock_critico():
#     inventario = cargar_inventario()
#     productos_criticos = []

#     for producto in inventario:
#         if producto["stock"] <= 3:
#             productos_criticos.append(producto)

#             return productos_criticos
# #------------------------------------------------------------------------------------------------------------------------------------------------
# @app.get("/productos/buscar/{palabra_clave}")
# def buscar_productos(palabra_clave: str):
#     inventario = cargar_inventario ()
#     resultados = []

#     for producto in inventario:
#         nombre = producto["nombre"]

#         if palabra_clave.lower() in nombre.lower():
#             resultados.append(producto)

#             return resultados

# @app.post("/productos", status_code=201)
# async def registrar_nuevo_producto(producto: ProductoCreate):
#     datos = await leer_base_datos()

#     #1. validar que el producto no exista
#     for dato in datos:
#         if dato["codigo"] == producto.codigo: 
#             raise HTTPException(status_code=400, detail="El codigo de producto ya existe.")

#          #2. convertir la clase a un diccionario
#     nuevo_producto = producto.model_dump

#         #3. guardar
#     datos.append(nuevo_producto)
#     await guardar_base_datos(datos)

#     return {"mensaje": "producto registrado correctamente", "producto": nuevo_producto}

# # Put, actulizar inventario
# @app.put("/productos/{codigo_producto}")
# async def actulizar_producto(codigo_producto: str, producto_actualizado: ProductoCreate):
#     datos = await leer_base_datos()
#     for posicion, dato in enumerate(datos):
#         if dato["codigo"] == codigo_producto:
#             # Reemplazamos los datos manteniendo el codigo
#             datos[posicion] = producto_actualizado.model_dump()
#             datos[posicion]["codigo"] = codigo_producto

#             await guardar_base_datos(datos)
#             return {"mensaje": "Producto actualizado", "producto": datos[posicion]}
        
#     raise HTTPException(status_code=404, detail="Producto no encontrado")




# ----------------------------------------------------------------------------------------------------------

from fastapi import FastAPI, HTTPException, status
from database import leer_datos, guardar_datos
from schemas import OrdenCreate, OrdenUpdate


app = FastAPI()

@app.post("/ordenes", status_code=status.HTTP_201_CREATED)
async def crear_orden(orden: OrdenCreate):
    ordenes = await leer_datos()
    placa_upper = orden.placa.upper()

    for o in ordenes:
        if o["placa"].upper() == placa_upper:
            if o["estado"].lower() != "entregada":
                raise HTTPException(
                    status_code=400,
                    detail="La moto ya se encuentra en el taller"
                )

    nueva_orden = {
        "placa": placa_upper,
        "modelo": orden.modelo,
        "falla_reportada": orden.falla_reportada,
        "estado": "En diagnóstico",
        "costo_reparacion": 0
    }

    ordenes.append(nueva_orden)
    await guardar_datos(ordenes)

    return {"mensaje": "Orden creada con éxito", "orden": nueva_orden}

@app.get("/ordenes")
async def consultar_ordenes():
    return await leer_datos()

@app.put("/ordenes/{placa}")
async def actualizar_orden(placa: str, datos_act: OrdenUpdate):
    ordenes = await leer_datos()
    orden_encontrada = None
    placa_upper = placa.upper()

    for o in ordenes:
        if o["placa"].upper() == placa_upper:
            orden_encontrada = o
            break

    if not orden_encontrada:
        raise HTTPException(
            status_code=404,
            detail="La orden con la placa especificada no existe"
        )

    if datos_act.nuevo_estado.lower() == "reparada" and datos_act.costo_reparacion <= 0:
        raise HTTPException(
            status_code=400,
            detail="No se puede marcar como reparada sin asignar un costo de reparación"
        )

    orden_encontrada["estado"] = datos_act.nuevo_estado
    orden_encontrada["costo_reparacion"] = datos_act.costo_reparacion

    await guardar_datos(ordenes)

    return {"mensaje": "Orden actualizada exitosamente", "orden": orden_encontrada}

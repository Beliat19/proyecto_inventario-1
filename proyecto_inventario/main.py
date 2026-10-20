from fastapi import FastAPI, HTTPException #importo mi framework
from database import leer_base_datos, obtener_producto
import json

# Inicializar la aplicación
app = FastAPI(
    title="API inventarios SENA",
    description="Mi primera API asíncrona",
    version="1.0.0"
)

def cargar_inventario():
    with open("inventario.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)

# Nuestro primer endpoint
@app.get("/") # Decorador -> Función que recibe como parámetro otra función
async def ruta_principal():
    return {"mensaje": "¡Bienvenido a mi primera API Rest!"}

@app.get("/estado")
async def estado_servidor():
    return {"status": "En línea", "servicios": "Operativos sin ningun invonveniente"}

@app.get("/productos")
async def listar_productos():
    datos = await leer_base_datos()
    return {"cantidad": len(datos), "productos": datos}

@app.get("/productos/{codigo_producto}")
async def buscar_un_producto(codigo_producto: str):
    try:
        # Para llamar a la función de obtener producto
        producto = await obtener_producto(codigo_producto)
        return producto
    except KeyError:
        raise HTTPException(status_code=404, detail="El producto soliciato no existe en la BD.")

    #--------------------------------------------------------------------------------------------------------------------------------------------

@app.get("/categorias")
def obtener_categorias():
    inventario = cargar_inventario()
    categorias = set()
    for producto in inventario:
        categorias.add(producto["categoria"])
    return list(categorias)

#------------------------------------------------------------------------------------------------------------------------------------------------
@app.get("/alertas/stock")

def obtener_stock_critico():
    inventario = cargar_inventario()
    productos_criticos = []

    for producto in inventario:
        if producto["stock"] <= 3:
            productos_criticos.append(producto)

            return productos_criticos
#------------------------------------------------------------------------------------------------------------------------------------------------
@app.get("/productos/buscar/{palabra_clave}")
def buscar_productos(palabra_clave: str):
    inventario = cargar_inventario ()
    resultados = []

    for producto in inventario:
        nombre = producto["nombre"]

        if palabra_clave.lower() in nombre.lower():
            resultados.append(producto)

            return resultados
        


import asyncio
import aiofiles
import json

#un diccionario en python es el equivalente a un objeto en js
inventario = [
    {"codigo": "PEP01", "nombre": "llanta ron 17", "stock": 10},
    {"codigo": "PEP02", "nombre": "aceite motul 7100", "stock":5},
]

async def guardar_inventario(datos,archivo):
    print("Guardando datos de formaasincronica...")
    async with aiofiles.open(archivo, mode="w", encoding='utf-8') as f:
        texto_json = json.dumps(datos, indent=4)
        await f.write(texto_json)
    print("inventario guardado en el disco")


async def cargar_inventario(archivo):
    print("cargando los datos el Json...")
    try:
        async with aiofiles.open(archivo, mode="r", encoding='utf-8')as archivo_json:
          texto_json = await archivo_json.read()
          datos = json.loads(texto_json)  #traducir de json a python
          return datos
    except FileNotFoundError:
        print("el archivo no existe.Iniciando con inventario vacio.")
        return []

async def main():
    #1.Guardar
    await guardar_inventario(inventario, 'inventario.json')

    #2.Leer
    datos_recuperados = await cargar_inventario('inventario.json')
    print("Datos recuperados: ", datos_recuperados)

    asyncio.run(main())
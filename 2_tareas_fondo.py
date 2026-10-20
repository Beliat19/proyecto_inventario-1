import asyncio
import time

async def enviar_correo_bienvenida(usuario):
    print(f"[{time.strftime('%X')}] PREPARANDO CORREO PARA {usuario}...")
    await asyncio.sleep(4)
    print(f"[{time.strftime('%X')}] Correo enviado exitosamente a {usuario}...")

async def registrar_usuario(usuario):
    print(f"[{time.strftime('%X')}] Guardando a {usuario} en la BD...")
    await asyncio.sleep(1)
    print(f"[{time.strftime('%X')}] {usuario} guardado en la BD...")
    tarea_correo = asyncio.create_task(enviar_correo_bienvenida(usuario))
    print(f"[{time.strftime('%X')}] Retornado respuesta al fontend: ¡Bienvenido {usuario}!")

    return tarea_correo

async def main():
    tarea = await registrar_usuario("juan.perez@seena.edu.co")

    #simulamos q el servidpr esta haciendo otras cosas
    print("el servidor sigue a otros clientes")
    await asyncio.sleep(5)
    #esperamos 5 segundos  a q termine todo el programa
 
asyncio.run(main())
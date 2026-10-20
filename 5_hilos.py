import asyncio
import time

def procesar_reporte_medico():
    print("Iniciando procesamiento de reporte (Bloqueo de sistema)...")
    time.sleep(3) #El tiempo que estara bloqueado
    print("Reporte generado.")
    return "reporte.pdf"

async def atender_cliente(cedula):
    print(f"Atendiendo al cliente {cedula} rapidamente...")
    await asyncio.sleep(1)
    print(f"Paciente {cedula} se ha dado de alta.")

async def main():
    #Trabajamos al reporte en un hilo secundario
    tarea_pesada = asyncio.to_thread(procesar_reporte_medico)
    tarea_clienes = [atender_cliente(i) for i in range(1, 4)]
    await asyncio.gather(tarea_pesada, *tarea_clientes)

asyncio.run(main())
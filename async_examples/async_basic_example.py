import asyncio
from time import perf_counter
from random import randint
from rich.console import Console

console = Console(color_system="windows")

async def requerer_dados():
    start_time = perf_counter()
    console.print("[magenta]PRIMEIRO -> [/magenta]")
    await asyncio.sleep(2)
    end_time = perf_counter()
    console.print(f"[magenta]-> PRIMEIRO[/magenta] Tempo decorrido: {end_time - start_time}")
    return {'data': [1,2,3,4,5]}



async def escrever_lista_de_arquivos():
    start_time = perf_counter()
    console.print("[green]SEGUNDO -> [/green]")

    for value in range(10):
        print(value)
        await asyncio.sleep(0.25)

    end_time = perf_counter()
    console.print(f"[green]-> SEGUNDO[/green] Tempo decorrido {end_time - start_time}")


async def executar_processamentos():

    tasks_1 = asyncio.create_task(requerer_dados())
    tasks_2 = asyncio.create_task(escrever_lista_de_arquivos())

    valor_da_task_1 = await tasks_1
    print(valor_da_task_1)
    # await tasks_2

if __name__ == "__main__":
    asyncio.run(executar_processamentos())
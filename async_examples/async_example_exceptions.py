import asyncio
from time import perf_counter
from random import randint
from rich.console import Console

console = Console(color_system="windows")

async def primero_processamento_demorado():
    start_time = perf_counter()
    console.print("[magenta]PRIMEIRO -> [/magenta] Requisitar algo para uma API.")
    await asyncio.sleep(randint(2, 10))
    end_time = perf_counter()
    console.print(f"[magenta]-> PRIMEIRO[/magenta] Tempo decorrido: {end_time - start_time}")

async def segundo_processamento_demorado():
    start_time = perf_counter()
    console.print("[green]SEGUNDO -> [/green] Enviar emails.")
    await asyncio.sleep(randint(2, 10))
    end_time = perf_counter()
    console.print(f"[green]-> SEGUNDO[/green] Tempo decorrido {end_time - start_time}")

async def terceiro_processamento_demorado():
    start_time = perf_counter()
    console.print("[yellow]TERCEIRO -> [/yellow] Salvar dados no banco.")
    await asyncio.sleep(randint(2, 10))
    end_time = perf_counter()
    console.print(f"[yellow]-> TERCEIRO[/yellow] Tempo decorrido {end_time - start_time}")

async def quarto_processamento_demorado():
    start_time = perf_counter()
    console.print("[blue]QUARTO -> [/blue] Puxar e manipular um Dataframe")
    await asyncio.sleep(randint(2, 10))
    end_time = perf_counter()
    console.print(f"[blue]-> QUARTO[/blue] Tempo decorrido {end_time - start_time}")

async def quinto_processamento_demorado():
    start_time = perf_counter()
    console.print("[red]QUINTO -> [/red] Estudar pra ficar monstro")
    await asyncio.sleep(10)
    end_time = perf_counter()
    console.print(f"[red]-> QUINTO[/red] Tempo decorrido {end_time - start_time}")

def executar_processamentos():
    # definindo um loop de eventos, responsável por controlar a execução das tarefas
    loop = asyncio.get_event_loop()

    # criação de lista de tarefas "esperáveis" a serem executadas
    tasks = [
        loop.create_task(primero_processamento_demorado()),
        loop.create_task(segundo_processamento_demorado()),
        loop.create_task(terceiro_processamento_demorado()),
        loop.create_task(quarto_processamento_demorado()),
        loop.create_task(quinto_processamento_demorado())
    ]

    esperaveis = asyncio.wait(tasks)

    loop.run_until_complete(esperaveis)

    loop.close()

if __name__ == "__main__":
    executar_processamentos()
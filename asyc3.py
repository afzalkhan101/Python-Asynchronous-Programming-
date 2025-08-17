import asyncio

async def task(name, sec):
    print(f"{name} started")
    await asyncio.sleep(sec)
    print(f"{name} finished after {sec} seconds")
    return name

async def main():
    results = await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 3),
        task("Task 3", 1)
    )
    print("All tasks done:", results)

asyncio.run(main())

import asyncio 

async def greet(name):

    await asyncio.sleep(2) #set sleep time for wait 2 sec . 

    print(f"{name}") 


async def main():
    
    await asyncio.gather(

        greet("Afzal"),
        greet("Khan")
    )

asyncio.run(main())

import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

    results = []
    async with asyncio.TaskGroup() as tg:
        results.append(tg.create_task(factorial("A", 2)).result())
        results.append(tg.create_task(factorial("B", 3)).result())
        results.append(tg.create_task(factorial("C", 4)))

    print([item.result() for item in results])

    print(L)

asyncio.run(main())
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(0.2)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 10),
        factorial("B", 30),
        factorial("C", 40),
    )
    print(L)


    results = []
    async with asyncio.TaskGroup() as tg:
        results.append(tg.create_task(factorial("A", 10)))
        results.append(tg.create_task(factorial("B", 30)))
        results.append(tg.create_task(factorial("C", 40)))

    print([item.result() for item in results])



if __name__ == '__main__':
    asyncio.run(main())
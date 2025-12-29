import asyncio
import time 

async def func1():
    print('func1 started execution')
    await asyncio.sleep(1)
    print('func1 comleted execution')
    
async def func2():
    print('func2 started execution')
    await asyncio.sleep(2)
    print('func2 comleted execution')

async def func3():
    print('func3 started execution')
    await asyncio.sleep(3)
    print('func3 comleted execution')


async def main():
    start = time.time()
    
    asyncio.create_task(func1())
    asyncio.create_task(func2())
    await asyncio.create_task(func3())
    
    print(f'Execution took {time.time() - start} s')
    
    
if __name__ == '__main__':
    asyncio.run(main())
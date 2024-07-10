from random import random
import asyncio

async def cook_dish(dish_name):
   
    cook_time = 1 + random()
    print(f'Microwave ({dish_name}): Cooking {cook_time:.2f} seconds...')
    await asyncio.sleep(cook_time)
    print(f'Microwave ({dish_name}): Finished cooking')
    return f'{dish_name} is completed',cook_time

async def main():
    
    dishes = ['Rice', 'Noodle', 'Curry']
    tasks = [asyncio.create_task(cook_dish(dish)) for dish in dishes]
    
    
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    
    for task in done:
        print(task.result())
    
    
    print(f'Uncompleted task: {len(pending)}')
        

asyncio.run(main())



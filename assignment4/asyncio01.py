# example of getting the current task from the main coroutine
import asyncio

# define a mian coroutine
async def main():
    # report a message
    print('main coroutine started')
    # get teh current task
    task = asyncio.current_task()
    # report its details
    print(task)

# started the asyncio program
asyncio.run(main())
#network request and reading files
import asyncio #many waiting tasks


#threads - to wait and share data (less cpu intensive , IO
# and processes  - CPU intensive computations


#so far this creates tasks and allows us waiting till it finishes
async def fetch_data(delay,id):
    print("Fetching data", id)
    await asyncio.sleep(delay)
    print("Data fetched")
    return {"data": "Some data"}


#coroutine function
async def main():
    #print("Hello world")
    #task = fetch_data(2)#has not been executed yet as it needs to be awaited
    #pausing till completion
    #result = await task
    
    task1 = asyncio.create_task(fetch_data(1,2)) #creating tasks allows it run simultaneously
    task2 = asyncio.create_task(fetch_data(2,3))
    
    #by placing it here, task3 would wait first for task1 and task2 completion
    #result1 = await task1
    #result2 = await task2
    
    task3 = asyncio.create_task(fetch_data(3,1))
    
    result1 = await task1
    result2 = await task2
    result3 = await task3



async def main2():
    #runs coroutines concurrently
    #gathers results in a list
    results = await asyncio.gather(fetch_data(1,2), fetch_data(2,1), fetch_data(3,3))
    
    for result in results:
        print(f"Received {result}")
        
        

async def main3():
    tasks = []
    #built in error handling- if any error in one task -all tasks cancelled
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2,1,3], start =1):
            task = tg.create_task(fetch_data(i,sleep_time))
            tasks.append(task)
    
    #at this point all tasks already executed
    #stop blocking
    
    results = [task.result() for task in tasks]
    
    for result in results:
        print(f"Received {result}")


""" _______________________________________________"""

async def set_future_result(future, value):
    await asyncio.sleep(2)
    future.set_result(value)
    print(f"Set the future's result to: {value}")
    
async def main4():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    
    asyncio.create_task(set_future_result(future, "Future result is ready"))
    result = await future
    print(f"REsult {result}")

""" _______________________________________________"""


shared_resources = 0

lock = asyncio.Lock()

async def modify_shared_rss():
    global shared_resources
    async with lock:#checks if any other coroutines are using this
    #if smth uses it, its gonna wait till it finishes
        #critical section starts
        print("Rss before modification", shared_resources)
        shared_resources +=1
        await asyncio.sleep(1)
        print("Rss after modification", shared_resources)
        
async def main5():
    await asyncio.gather(*(modify_shared_rss() for _ in range(5)))

""" _______________________________________________"""

async def access_rss(semaphore, resource_id):
    async with semaphore:
        print(f"accessing {resource_id}")
        await asyncio.sleep(1)
        print(f"releasing {resource_id}")
        
async def main6():
    semaphore = asyncio.Semaphore(2)#allows 2 concurrent accesses (network requests??)
    await asyncio.gather(*(access_rss(semaphore,i) for i in range(5)))


""" _______________________________________________"""


#synchronisation
async def waiter(event):
    #waiting for the event to be set
    await event.wait()
    #event has been set
    
async def setter(event):
    await asyncio.sleep(2)
    event.set()
    print("event has been set")
    
async def main7():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))



""" _______________________________________________"""

#handles waiting
asyncio.run(main())#starts coroutine function

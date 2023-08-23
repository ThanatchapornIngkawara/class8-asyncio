# we will create a producer coroutine that will generate ten random numbers 
# and put them on the queue. We will also create a consumer coroutine 
# that will get numbers from the queue and report their values.

import asyncio
import time
from random import random

# coroutine to generate work
async def producer(queue):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()  
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue
        await queue.put(value)  

    await queue.put(None)  
    print(f'{time.ctime()} Producer: Done')

# coroutine to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consum work
    while True:
        # get a unit of work
        item = await queue.get()
        # check for stop signal  
        if item is None:
            break
        # report  
        print(f'{time.ctime()} > got {item}')  
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

# start the asyncio program
asyncio.run(main())


# Wed Aug 23 14:14:17 2023 Producer: Running
# Wed Aug 23 14:14:17 2023 Consumer: Running
# Wed Aug 23 14:14:18 2023 > got 0.558587109215894
# Wed Aug 23 14:14:18 2023 > got 0.2672822107403703
# Wed Aug 23 14:14:19 2023 > got 0.9986519569585752
# Wed Aug 23 14:14:20 2023 > got 0.34952455243884184
# Wed Aug 23 14:14:20 2023 > got 0.06358351649839789
# Wed Aug 23 14:14:21 2023 > got 0.986159281428222
# Wed Aug 23 14:14:21 2023 > got 0.7216200556298227
# Wed Aug 23 14:14:22 2023 > got 0.5200714207445464
# Wed Aug 23 14:14:22 2023 > got 0.06925104817700867
# Wed Aug 23 14:14:23 2023 Producer: Done
# Wed Aug 23 14:14:23 2023 > got 0.8874836850107667
# Wed Aug 23 14:14:23 2023 Consumer: Done
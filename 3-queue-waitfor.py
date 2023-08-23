import asyncio
import time
from random import random

# Coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()  
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue  
        await queue.put(value)  
    # send an all done signal
    await queue.put(None)  
    print(f'{time.ctime()} Producer: Done')

# consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        try:
            item = await asyncio.wait_for(queue.get(), timeout=0.5)
        except asyncio.TimeoutError:
            print(f'{time.ctime()} Consumer: gave up waiting...')
            continue
        # Check for stop
        if item is None:
            break
        # report  
        print(f'{time.ctime()} > got {item}')  
    print('Consumer: Done')

# Entry point coroutine
async def main():
    # Create the shared queue
    queue = asyncio.Queue()
    # Run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

# Start the asyncio program
asyncio.run(main())



# Producer: Running
# Wed Aug 23 14:19:47 2023 Consumer: Running
# Wed Aug 23 14:19:48 2023 Consumer: gave up waiting...
# Wed Aug 23 14:19:48 2023 > got 0.5278820812466577
# Wed Aug 23 14:19:48 2023 Consumer: gave up waiting...
# Wed Aug 23 14:19:48 2023 > got 0.7412519502304207
# Wed Aug 23 14:19:48 2023 > got 0.03543935599876158
# Wed Aug 23 14:19:49 2023 Consumer: gave up waiting...
# Wed Aug 23 14:19:49 2023 > got 0.8301545757713941
# Wed Aug 23 14:19:50 2023 Consumer: gave up waiting...
# Wed Aug 23 14:19:50 2023 > got 0.7836618485367339
# Wed Aug 23 14:19:50 2023 > got 0.26636705462411525
# Wed Aug 23 14:19:51 2023 Consumer: gave up waiting...
# Wed Aug 23 14:19:51 2023 > got 0.8540141533180232
# Wed Aug 23 14:19:52 2023 > got 0.28585793636119383
# Wed Aug 23 14:19:52 2023 > got 0.06991569348731874
# Wed Aug 23 14:19:52 2023 Producer: Done
# Wed Aug 23 14:19:52 2023 > got 0.4579362934622331
# Consumer: Done
from random import random 
import time
import asyncio

# coroutine to generate work 
async def producer (queue): 
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
    await queue.put (None) 
    print (f'{time.ctime()} Producer: Done')

# coroutine to consume work 
async def consumer(queue):
    print('Consumer: Running')
    #consume work
    while True:
        # get a unit of work without blocking 
        try:
            item = queue.get_nowait() 
        except asyncio.QueueEmpty:
            print(f'{time.ctime()} Consumer: got nothing, waiting a while...') 
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print (f'{time.ctime()} >got {item}')
    # all done
    print (f'{time.ctime()} Consumer: Done')

# entry point coroutine 
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers 
    await asyncio.gather (producer(queue), consumer(queue))
# start the asyncio program 
asyncio.run(main())



# Producer: Running
# Consumer: Running
# Wed Aug 23 14:17:25 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:17:26 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:17:26 2023 >got 0.8469684161664557
# Wed Aug 23 14:17:26 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:17:27 2023 >got 0.2984616590548851
# Wed Aug 23 14:17:27 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:17:27 2023 >got 0.8307657823751406
# Wed Aug 23 14:17:27 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:17:28 2023 >got 0.5494112430707287
# Wed Aug 23 14:17:28 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:17:28 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:17:29 2023 >got 0.9538581586351509
# Wed Aug 23 14:17:29 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:17:29 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:17:30 2023 >got 0.7253606902139
# Wed Aug 23 14:17:30 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:17:31 2023 >got 0.39277479909922186
# Wed Aug 23 14:17:31 2023 >got 0.002802207103870913
# Wed Aug 23 14:17:31 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:17:31 2023 >got 0.787173840905841
# Wed Aug 23 14:17:31 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:17:31 2023 Producer: Done
# Wed Aug 23 14:17:32 2023 >got 0.5008178818753556
# Wed Aug 23 14:17:32 2023 Consumer: Done

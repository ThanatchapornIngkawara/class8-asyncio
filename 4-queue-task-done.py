from random import random
import asyncio 
import time

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
    print (f'{time.ctime()} Producer: Done')

# coroutine to consume work 
async def consumer(queue):
    print (f'{time.ctime()} Consumer: Running') 
    # consume work 
    while True:
        # get a unit of work.
        item = await queue.get()
        # report 
        print (f'{time.ctime()} >got {item}') 
        # block while processing
        if item:
            await asyncio.sleep(item) 
            # mark the task as done 
            queue.task_done()
# entry point coroutine 
async def main():
    # create the shared queue 
    queue =asyncio.Queue()
    #  start the consumer
    _ = asyncio.create_task(consumer(queue)) 
    # start the producer and wait for it to finish 
    await asyncio.create_task(producer(queue)) 
    #wait for all items to be processed 
    await queue.join()

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:32:40 2023 Consumer: Running
# Wed Aug 23 14:32:40 2023 Producer: Running
# Wed Aug 23 14:32:40 2023 >got 0.14713406428825937
# Wed Aug 23 14:32:40 2023 >got 0.24504786166240233
# Wed Aug 23 14:32:40 2023 >got 0.1862024886230228
# Wed Aug 23 14:32:41 2023 >got 0.8533874609987753
# Wed Aug 23 14:32:42 2023 >got 0.4813113742586941
# Wed Aug 23 14:32:43 2023 >got 0.6184469039177147
# Wed Aug 23 14:32:43 2023 >got 0.06916626400340964
# Wed Aug 23 14:32:43 2023 >got 0.9903001316651872
# Wed Aug 23 14:32:44 2023 >got 0.9466283669375218
# Wed Aug 23 14:32:45 2023 Producer: Done
# Wed Aug 23 14:32:45 2023 >got 0.8734718006718619

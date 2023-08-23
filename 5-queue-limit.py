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
        # add to the queue, may block  
        await queue.put(value)  
    print(f'{time.ctime()} Producer: Done')

# coroutine to 
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        # report
        print(f'{time.ctime()} > got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
            # mark as completed
            queue.task_done()
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # create many producers
    producers = [producer(queue) for _ in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # wait for the consumer to process all items
    await queue.join()

# start the asyncio program
asyncio.run(main())


# Wed Aug 23 14:24:10 2023 Consumer: Running
# Wed Aug 23 14:24:10 2023 Producer: Running
# Wed Aug 23 14:24:10 2023 Producer: Running
# Wed Aug 23 14:24:10 2023 Producer: Running
# Wed Aug 23 14:24:10 2023 Producer: Running
# Wed Aug 23 14:24:10 2023 Producer: Running
# Wed Aug 23 14:24:10 2023 > got 0.07493947563861458
# Wed Aug 23 14:24:10 2023 > got 0.3857233654702287
# Wed Aug 23 14:24:11 2023 > got 0.03925673984989109
# Wed Aug 23 14:24:11 2023 > got 0.5539061777420057
# Wed Aug 23 14:24:11 2023 > got 0.7185536393253465
# Wed Aug 23 14:24:12 2023 > got 0.3289826491091078
# Wed Aug 23 14:24:12 2023 > got 0.7750741453806396
# Wed Aug 23 14:24:13 2023 > got 0.6988780721102754
# Wed Aug 23 14:24:14 2023 > got 0.2537683244462712
# Wed Aug 23 14:24:14 2023 > got 0.7812479060482549
# Wed Aug 23 14:24:15 2023 > got 0.7788510703306373
# Wed Aug 23 14:24:16 2023 > got 0.9642258523273642
# Wed Aug 23 14:24:17 2023 > got 0.024084323935876784
# Wed Aug 23 14:24:17 2023 > got 0.7324274739982447
# Wed Aug 23 14:24:17 2023 > got 0.39306296153196285
# Wed Aug 23 14:24:18 2023 > got 0.49394784273070536
# Wed Aug 23 14:24:18 2023 > got 0.2668359109351979
# Wed Aug 23 14:24:19 2023 > got 0.503001476246526
# Wed Aug 23 14:24:19 2023 > got 0.7756464230255623
# Wed Aug 23 14:24:20 2023 > got 0.5774917265214131
# Wed Aug 23 14:24:21 2023 > got 0.6018539855640261
# Wed Aug 23 14:24:21 2023 > got 0.7090143001107588
# Wed Aug 23 14:24:22 2023 > got 0.5989748666001571
# Wed Aug 23 14:24:22 2023 > got 0.07701960396528384
# Wed Aug 23 14:24:23 2023 > got 0.8881938193769984
# Wed Aug 23 14:24:23 2023 > got 0.731521120441267
# Wed Aug 23 14:24:24 2023 > got 0.0534409813868445
# Wed Aug 23 14:24:24 2023 > got 0.7510856082496011
# Wed Aug 23 14:24:25 2023 > got 0.897540444351
# Wed Aug 23 14:24:26 2023 > got 0.7898802126032475
# Wed Aug 23 14:24:27 2023 > got 0.7839563165936221
# Wed Aug 23 14:24:28 2023 > got 0.9360151527804829
# Wed Aug 23 14:24:28 2023 > got 0.057141635051554784
# Wed Aug 23 14:24:29 2023 > got 0.24421342485307784
# Wed Aug 23 14:24:29 2023 > got 0.8930373949855417
# Wed Aug 23 14:24:30 2023 > got 0.547058632481961
# Wed Aug 23 14:24:30 2023 > got 0.7525494569955965
# Wed Aug 23 14:24:30 2023 Producer: Done
# Wed Aug 23 14:24:31 2023 > got 0.07301338723884865
# Wed Aug 23 14:24:31 2023 > got 0.9368250832374608
# Wed Aug 23 14:24:32 2023 > got 0.21999493393548508
# Wed Aug 23 14:24:32 2023 Producer: Done
# Wed Aug 23 14:24:32 2023 > got 0.17411234777560203
# Wed Aug 23 14:24:32 2023 > got 0.8979717409979913
# Wed Aug 23 14:24:32 2023 Producer: Done
# Wed Aug 23 14:24:33 2023 > got 0.16344549533654185
# Wed Aug 23 14:24:34 2023 > got 0.5539698704000952
# Wed Aug 23 14:24:34 2023 > got 0.9922457622802549
# Wed Aug 23 14:24:35 2023 > got 0.48475809362515065
# Wed Aug 23 14:24:36 2023 > got 0.3901039214342734
# Wed Aug 23 14:24:36 2023 Producer: Done
# Wed Aug 23 14:24:36 2023 > got 0.6499166639072866
# Wed Aug 23 14:24:36 2023 Producer: Done
# Wed Aug 23 14:24:37 2023 > got 0.6714594215168807
# Wed Aug 23 14:24:37 2023 > got 0.7061095717835314




from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue, id):
    print(f'{time.ctime()} Producer: Running')
     # generate work
    for i in range(10):
         # generate a value
        value = random() 
        # block to simulate work
        await asyncio.sleep((id+1)*0.1)
        # add to the queue, may block  
        await queue.put(value)  
    print(f'{time.ctime()} Producer: {id} Done')

# coroutine to 
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        # report
        print(f'{time.ctime()} > got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
            # mark as completed
            queue.task_done()
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # create many producers
    producers = [producer(queue, i) for i in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # wait for the consumer to process all items
    await queue.join()

# start the asyncio program
asyncio.run(main())


# Wed Aug 23 15:27:09 2023 Consumer: Running
# Wed Aug 23 15:27:09 2023 Producer: Running
# Wed Aug 23 15:27:09 2023 Producer: Running
# Wed Aug 23 15:27:09 2023 Producer: Running
# Wed Aug 23 15:27:09 2023 Producer: Running
# Wed Aug 23 15:27:09 2023 Producer: Running
# Wed Aug 23 15:27:09 2023 > got 0.13718138858164775
# Wed Aug 23 15:27:09 2023 > got 0.37466096121439396
# Wed Aug 23 15:27:09 2023 > got 0.33691807220906667
# Wed Aug 23 15:27:09 2023 > got 0.9519533637783019
# Wed Aug 23 15:27:10 2023 > got 0.4463728107370267
# Wed Aug 23 15:27:11 2023 > got 0.17862757370588556
# Wed Aug 23 15:27:11 2023 > got 0.981573361580362
# Wed Aug 23 15:27:12 2023 > got 0.856693487090431
# Wed Aug 23 15:27:13 2023 > got 0.0007416659634604805
# Wed Aug 23 15:27:13 2023 > got 0.9407716792227899
# Wed Aug 23 15:27:14 2023 > got 0.38267587851638474
# Wed Aug 23 15:27:14 2023 > got 0.867853723852242
# Wed Aug 23 15:27:15 2023 > got 0.21834735771316327
# Wed Aug 23 15:27:15 2023 > got 0.5635944662159753
# Wed Aug 23 15:27:16 2023 > got 0.9321609005900292
# Wed Aug 23 15:27:17 2023 > got 0.7347113697949017
# Wed Aug 23 15:27:18 2023 > got 0.843533682267392
# Wed Aug 23 15:27:19 2023 > got 0.6689421145839164
# Wed Aug 23 15:27:19 2023 > got 0.20882279677081717
# Wed Aug 23 15:27:19 2023 > got 0.7139918070139599
# Wed Aug 23 15:27:20 2023 > got 0.10914156582510792
# Wed Aug 23 15:27:20 2023 > got 0.1817725468143072
# Wed Aug 23 15:27:20 2023 > got 0.03338741072847207
# Wed Aug 23 15:27:21 2023 > got 0.8990896966980675
# Wed Aug 23 15:27:21 2023 > got 0.4355432094611119
# Wed Aug 23 15:27:22 2023 > got 0.8357536117211211
# Wed Aug 23 15:27:23 2023 > got 0.5384422870478592
# Wed Aug 23 15:27:23 2023 > got 0.3217365170600942
# Wed Aug 23 15:27:24 2023 > got 0.663210303078803
# Wed Aug 23 15:27:24 2023 > got 0.2722033463492636
# Wed Aug 23 15:27:24 2023 > got 0.32085005539131195
# Wed Aug 23 15:27:25 2023 > got 0.6784634826763802
# Wed Aug 23 15:27:26 2023 > got 0.1010735322162053
# Wed Aug 23 15:27:26 2023 > got 0.9117039739026522
# Wed Aug 23 15:27:27 2023 > got 0.7094383276826824
# Wed Aug 23 15:27:27 2023 Producer: 0 Done
# Wed Aug 23 15:27:27 2023 > got 0.8320145402475181
# Wed Aug 23 15:27:28 2023 > got 0.8420478461007637
# Wed Aug 23 15:27:29 2023 > got 0.02602379285040468
# Wed Aug 23 15:27:29 2023 > got 0.17857785015083005
# Wed Aug 23 15:27:29 2023 > got 0.7268226712324766
# Wed Aug 23 15:27:30 2023 > got 0.9733812572724649
# Wed Aug 23 15:27:31 2023 > got 0.7330606763050659
# Wed Aug 23 15:27:31 2023 Producer: 1 Done
# Wed Aug 23 15:27:32 2023 > got 0.9728442990595507
# Wed Aug 23 15:27:33 2023 > got 0.7083521203027607
# Wed Aug 23 15:27:33 2023 > got 0.7621758420634561
# Wed Aug 23 15:27:33 2023 Producer: 2 Done
# Wed Aug 23 15:27:34 2023 > got 0.8692341789869005
# Wed Aug 23 15:27:35 2023 > got 0.1562426941497086
# Wed Aug 23 15:27:35 2023 Producer: 3 Done
# Wed Aug 23 15:27:35 2023 > got 0.08928015345922091
# Wed Aug 23 15:27:35 2023 Producer: 4 Done
# Wed Aug 23 15:27:35 2023 > got 0.5755305210897662
# Wed Aug 23 15:27:36 2023 > got 0.8442287476933099

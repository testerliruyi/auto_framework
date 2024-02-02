import time
import asyncio

async def wait1():
    print("wait_1 start")
    await asyncio.sleep(1)
    print("await_1 end")
async def wait3():
    print("wait_3 start")
    await asyncio.sleep(3)
    print("await_3 end")
async def wait5():
    print("wait_5 start")
    await asyncio.sleep(5)
    print("await_5 end")

tasks = [
    wait1(),
    wait3(),
    wait5()
]

if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    startTime = time.time()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    endTime= time.time()
    print("final time:",endTime -startTime)


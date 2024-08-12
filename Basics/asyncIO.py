import asyncio

import requests 

url = "https://pixabay.com/photos/arc-de-triomphe-architecture-vaulted-4069577/"

async def function1():
    response = requests.get(url)    
    open("instagram.jpg", "wb").write(response.content)
    print("func 1")

    
async def function2():
    response = requests.get(url)
    open("instagram2.jpg", "wb").write(response.content)
    print("func 2")

    
async def function3():    
    response = requests.get(url)
    open("instagram3.jpg", "wb").write(response.content)
    print("func 3")
    
    
async def main():
    # task = asyncio.create_task(function1())
    # await function2()
    # await function3()
    
    await function1()
    await function3()  
    await function2()
    
    # L = await asyncio.gather(
    #     function1(),
    #     function2(),
    #     function3(),  
    # )
    
    # print(L)
    
asyncio.run(main())
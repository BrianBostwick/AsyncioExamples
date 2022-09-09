
#! python3

#
#Simple asyncio program that prints a list of number in order, with each number haveing a delay
# set by a random time between 1ms-10ms.
#

__author__ = "Brian Bostwick"
__license__ = "GPL"
__version__ = "1.0.1"

import asyncio
import random

def main():
    #Function to be added to the async event loop.
    async def print_rand( call ):

        #Generate a random number to set as the delay.
        time = random.randint(0,10)
        #Delay for time, then print the delay time and call number.
        await asyncio.sleep( time*1e-3 )
        print(f"Waited for {time} ms. Called {call+1}.")

    async def get_events( n ):

        #Events add each task to the event look in a list.
        events = [ asyncio.create_task( print_rand(i) ) for i in range(n) ]
        #Run the list of events and does so asynchronously
        completed, pending = await asyncio.wait(events)

    #Create event loop.
    loop = asyncio.get_event_loop()
    #Adds the number of instances of the code to the event loop and runs the code.
    loop.run_until_complete( get_events( 5 ) )
    #Deconstructs event loop.
    loop.close()

if __name__ == "__main__":
    main()

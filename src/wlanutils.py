from pyrcrack import AirmonNg, AirodumpNg, MONITOR
import asyncio

#Just an arbitrary change to test something

airmon = AirmonNg()

async def getInterfaces():
    print("Querying available interfaces")
    interfaces = await airmon.interfaces
    if (interfaces):
        print("Available interfaces: " + str([interface.asdict() for interface in interfaces]))
    else:
        print("No interfaces found")
    availableInterfaces = [x.interface for x in interfaces]
    return(availableInterfaces)

async def testMonInterface(iface):
    async with airmon(iface) as mon:
        if (MONITOR.get()):
            print("Success, monitor interface is " + MONITOR.get())
            return(True)
        else:
            print("Failed to put " + iface + " in monitor mode")
            return(False)
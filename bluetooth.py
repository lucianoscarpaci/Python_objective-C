from objc_util import *

# Load the CoreBluetooth framework
CBPeripheralManager = ObjCClass('CBPeripheralManager')
CBManager = ObjCClass('CBManager')

# Check if Bluetooth is powered on
cb_manager = CBManager.alloc().init()
if cb_manager.state() == 5:  # Bluetooth powered on (state 5)
    # Get a list of connected peripherals
    cb_manager = CBManager.alloc().init()
    connected_devices = cb_manager.retrieveConnectedPeripherals()

    # Check if connected device named 'Heyday' is found
    heyday_connected = any(device.name for device in connected_devices if 'Heyday' in device.name)
    if heyday_connected:
        print("Connected to Heyday wireless earbuds.")
        # Add your reminder logic here
    else:
        print("Not connected to Heyday wireless earbuds.")
else:
    print("Bluetooth is not turned on.")

# CB is the CoreBluetooth framework, i just found out import cb is the correct way to use it.
# also a delegate needs to be created to use bluetooth
# so far i need to get the bluetooth state to powered on.
# search for the name of the device which is 'Heyday'.
# Old code is still here, but i will try to implement the new code.
# broken code, i will try to fix it.
from objc_util import *

# Load the bluetooth
CBCentralManager = ObjCClass('CBCentralManager')

cb_manager = CBCentralManager.alloc().init()

print(cb_manager.state())
# CBManagerState powered on
if cb_manager.state() == 0:
    print('Bluetooth is on')
    print('Connected to Heyday Wireless Earbuds')
else:
    print("Bluetooth is not turned on")
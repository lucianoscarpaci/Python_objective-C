'''
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

import cb

class HeydayCentralManagerDelegate (object):
    def __init__(self):
        self.peripheral = None

    def did_discover_peripheral(self, p):
        print('Discovered peripheral:', p.name)
        if p.name and 'HEYDAY' in p.name and not self.peripheral:
            self.peripheral = p
            cb.connect_peripheral(p)

    def did_connect_peripheral(self, p):
        print('Connected:', p.name)
        print('Discovering services...')
        p.discover_services()

    def did_fail_to_connect_peripheral(self, p, error):
        print('Failed to connect: %s' % (error,))

    def did_disconnect_peripheral(self, p, error):
        print('Disconnected, error: %s' % (error,))
        self.peripheral = None

delegate = HeydayCentralManagerDelegate()
cb.set_central_delegate(delegate)
cb.scan_for_peripherals()
'''
import cb

class HeydayCentralManagerDelegate (object):
    def __init__(self):
        self.peripheral = None

    def did_discover_peripheral(self, p):
        print('Discovered peripheral:', p.name)
        if p.name and '110033_DFBC' in p.name and not self.peripheral:
            self.peripheral = p
            cb.stop_scan()
            print('Connecting to peripheral:', p.name)
            cb.connect_peripheral(p)

    def did_connect_peripheral(self, p):
        print('Connected:', p.name)
        print('Discovering services...')
        p.discover_services()

    def did_fail_to_connect_peripheral(self, p, error):
        print('Failed to connect: %s' % (error,))
        self.peripheral = None
        cb.scan_for_peripherals()

    def did_disconnect_peripheral(self, p, error):
        print('Disconnected, error: %s' % (error,))
        self.peripheral = None
        cb.scan_for_peripherals()

    def did_discover_services(self, p, error):
        if error:
            print('Error discovering services: %s' % (error,))
            return
        for s in p.services:
            print('Discovered service:', s.uuid)
            p.discover_characteristics(s)

    def did_discover_characteristics(self, s, error):
        if error:
            print('Error discovering characteristics: %s' % (error,))
            return
        for c in s.characteristics:
            print('Discovered characteristic:', c.uuid)

delegate = HeydayCentralManagerDelegate()
cb.set_central_delegate(delegate)

# Ensure Bluetooth is powered on
if cb.get_state() != cb.CM_STATE_POWERED_ON:
    print("Bluetooth is not powered on")
else:
    print("Scanning for peripherals...")
    cb.scan_for_peripherals()

# Keep the script running
import time
while True:
    time.sleep(1)

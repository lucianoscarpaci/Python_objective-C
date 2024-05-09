# coding: utf-8

'''Simple demo of using UIDevice to query the current battery state'''

from objc_util import *
import platform


class BatteryDisplay:
    def __init__(self):
        self.UIDevice = ObjCClass('UIDevice')
        self.device = self.UIDevice.currentDevice()
        self.device.setBatteryMonitoringEnabled_(True)
        self.battery_states = {1: '🔋 unplugged', 2: '⚡️ charging', 3: '✅ full'}

    def get_battery_info(self):
        battery_percent = self.device.batteryLevel() * 100
        state = self.device.batteryState()
        return (battery_percent, state)

    def display(self):
        battery_percent, state = self.get_battery_info()
        if state == 2:
            print('⚡️ Charging...')
            print('🔋 Battery level: %0.1f%%' % (battery_percent))
        elif state == 3:
            print('✅ Full...')
            print('🔋 Battery level: %0.1f%%' % (battery_percent))
        else:
            print('🔌 Not charging...')
            print('🔋 Battery level: %0.1f%%' % (battery_percent))

    def __del__(self):
        self.device.setBatteryMonitoringEnabled_(False)


class systemDisplay:
    def __init__(self):
        self.UIDevice = ObjCClass('UIDevice')
        self.device = self.UIDevice.currentDevice()
        self.iPhone = self.device.localizedModel()
        self.software = self.device.systemVersion()
        self.kernel = platform.system()
        self.release = platform.release()
        self.cpu = platform.uname()

    def get_cpu_info(self):
        info = self.cpu
        if info[0] == 'Darwin':
        	cpu_info = info[3].split()[10]
        	return cpu_info
        else:
        	return 'Unknown'

    def display(self):
    	print('📱', self.iPhone, self.software)
    	print('📦', self.kernel, self.release)
    	print('🔧', self.get_cpu_info())


monitor = BatteryDisplay()
monitor.get_battery_info()
monitor.display()
system_info = systemDisplay()
system_info.display()
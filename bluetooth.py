import cb
import time


class HeydayCentralManagerDelegate:
    def __init__(self):
        self.heyday = None

    def is_bluetooth_enabled(self):
        if cb.get_state() != cb.CM_STATE_POWERED_ON:
            time.sleep(1)
            if cb.get_state() != cb.CM_STATE_POWERED_ON:
                time.sleep(1)
            else:
                print("Heyday earbuds are connected")
        else:
            print("Heyday earbuds are connected")


delegate = HeydayCentralManagerDelegate()
cb.set_central_delegate(delegate)
delegate.is_bluetooth_enabled()

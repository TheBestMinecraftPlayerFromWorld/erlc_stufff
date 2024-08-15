import time
from python_hue_v2 import Hue,BridgeFinder
from time import localtime, strftime

finder = BridgeFinder()
time.sleep(1)  # wait for search
# Get server by mdns
#host_name = finder.get_bridge_server_lists()[0]  # Here we use first Hue Bridge

hue = Hue("192.168.1.100","4YhSKSbjDjZtBsEC75KLyc2Wg957CdIrAko4FFz6")
lights  = hue.lights
lightsZimmer = []
def switchLights():
    brightness = 100
    if localtime().tm_hour>=17:
        brightness = 50
    for light in lights:
        try:
            if light.light_id in lightsZimmer:
                light.on = not light.on
                light.brightness = brightness
                light.color_xy = (0.1,0.3)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(e)

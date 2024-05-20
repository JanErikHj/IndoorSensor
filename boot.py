import network
import utilities.config as config

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(config.SSID, config.AUTH)

print()
print("Connected to ",config.SSID)
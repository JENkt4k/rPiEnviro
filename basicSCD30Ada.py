# import board
import adafruit_scd30
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

bus = SMBus(1)
scd = adafruit_scd30.SCD30(bus)
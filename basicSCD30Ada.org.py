import time
import board
import adafruit_scd30

scd = adafruit_scd30.SCD30(board.I2C())

# scd.temperature_offset = 10
print("Temperature offset:", scd.temperature_offset)

# scd.measurement_interval = 4
print("Measurement interval:", scd.measurement_interval)

# scd.self_calibration_enabled = True
print("Self-calibration enabled:", scd.self_calibration_enabled)

# scd.ambient_pressure = 1100
print("Ambient Pressure:", scd.ambient_pressure)

# scd.altitude = 100
print("Altitude:", scd.altitude, "meters above sea level")

# scd.forced_recalibration_reference = 409
print("Forced recalibration reference:", scd.forced_recalibration_reference)
print("")

while True:
    data = scd.data_available
    if data:
        print("Data Available!")
        print("CO2:", scd.CO2, "PPM")
        print("Temperature:", scd.temperature, "degrees C")
        print("Humidity::", scd.relative_humidity, "%%rH")
        print("")
        print("Waiting for new data...")
        print("")

    time.sleep(0.5)
# SPDX-FileCopyrightText: Copyright (c) 2025 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time

import board

import adafruit_lps28

i2c = board.I2C()
sensor = adafruit_lps28.LPS28(i2c)

print("LPS28 Simple Test")
print("-" * 40)

while True:
    if sensor.data_ready:
        print(f"Converted Pressure: {sensor.pressure:.1f} hPa")
        print(f"Converted Temperature: {sensor.temperature:.1f} °C")
        print("-" * 40)

    time.sleep(0.5)

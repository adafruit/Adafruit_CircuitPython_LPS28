# SPDX-FileCopyrightText: Copyright (c) 2025 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time

import board

import adafruit_lps28

i2c = board.I2C()
sensor = adafruit_lps28.LPS28(i2c)

sensor.data_rate = 4  # 4 Hz data rate for one-shot mode
sensor.averaging = 512  # Average 512 samples

while True:
    # Trigger one-shot measurement
    sensor.trigger_one_shot = True

    # Wait for data ready
    if sensor.data_ready:  # Check PRESS_READY bit
        print(f"Pressure: {sensor.pressure:.1f} hPa")
        print(f"Temperature: {sensor.temperature:.1f} °C")
        print("-" * 40)

# SPDX-FileCopyrightText: Copyright (c) 2025 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_lps28

i2c = board.I2C()
sensor = adafruit_lps28.LPS28(i2c)

sensor.data_rate = 200
sensor.averaging = 32
sensor.fifo_watermark_int = True
sensor.fifo_mode = 'CONTINUOUS'
sensor.fifo_watermark = 10

while True:
    if sensor.fifo_ready:  # Check watermark flag
        samples = sensor.fifo_unread_samples
        print(f"FIFO unread samples: {samples}")
        for _ in range(samples):
            pressure = sensor.fifo_pressure
            print(f"FIFO Pressure (hPa): {pressure:.2f}")
    time.sleep(0.1)
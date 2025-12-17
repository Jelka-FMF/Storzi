import os
import time

with open(os.environ["JELKA_POSITIONS"]) as file:
    n = len(file.readlines())

print(f'#{{"version": 0, "led_count": {n}, "fps": 1}}')

while True:
    print("#" + "000000" * n)
    time.sleep(1)

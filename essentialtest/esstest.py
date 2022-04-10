import random
import time

def ticksleep():
    time.sleep(0.05)

x = str(random.randrange(10))

for j in range(100):
    print(f"{x}")
    x = str(random.randrange(10))
    ticksleep()

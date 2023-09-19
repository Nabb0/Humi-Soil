import RPi.GPIO as GPIO
import time
import random


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

print("LED intermittenza")


random_number = random.randint(1, 10)
print(random_number)
    # Genera un numero casuale compreso tra 1 e 10

if random_number % 2 == 0:
    print("LED on")
    GPIO.output(18, GPIO.HIGH)
else:
    print("LED off")
    GPIO.output(18, GPIO.LOW)

time.sleep(1)
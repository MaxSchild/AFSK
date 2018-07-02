#importieren
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

clock = 21
output_enable = 20
write_enable = 16
reset = 5

GPIO.setup(clock, GPIO.OUT)
GPIO.setup(output_enable, GPIO.OUT)
GPIO.setup(write_enable, GPIO.OUT)
GPIO.setup(reset, GPIO.OUT)

# Reset durchfuehren
GPIO.output(reset, GPIO.HIGH)
time.sleep(0.1)
GPIO.output(reset, GPIO.LOW)

GPIO.output(output_enable, GPIO.LOW)
GPIO.output(write_enable, GPIO.HIGH)
while True:
		#clock um 1 erhöhen
	GPIO.output(clock, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(clock, GPIO.LOW)
	time.sleep(0.1)
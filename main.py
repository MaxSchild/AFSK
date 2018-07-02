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

GPIO.output(output_enable, GPIO.HIGH)
GPIO.output(write_enable, GPIO.LOW)

# Reset durchfuehren
GPIO.output(reset, GPIO.HIGH)
time.sleep(0.1)
GPIO.output(reset, GPIO.LOW)

#pins erstellen

#adressPins (maximal 15)
adressPins = []
#outputPins(maximal 8)
outputPins = [2, 3, 4, 17, 6, 13, 19, 26]
for i in outputPins:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.LOW)

outputWert = [0, 0, 0, 0, 0, 0, 0, 0]
#daten erstellen bzw von anderer Datei einlesen
nachrichtArray = []
for i in range(0, 256):
	nachrichtArray.append(i)
#print(nachrichtArray[len(nachrichtArray) - 1])
#schreiben


for i in nachrichtArray:
	nachricht = bin(i)
	print(nachricht)
	ersterBit = 8 - (len(nachricht) - 2)
	#ersten zwei Zeichen gehoeren nicht zu den Bits
	for j in range(0, len(nachricht) - 2): 
		outputWert[ersterBit + j] = int(nachricht[j + 2])
		#print(outputPins[ersterBit + j])

	#WritePin setzen
	#time.sleep(0.2)

	for k in range(len(outputPins)):
		#print(type(outputPins[k]), type(outputWert[k]), outputWert[k])
		GPIO.output(outputPins[k], outputWert[k])

	#clock um 1 erhöhen
	GPIO.output(clock, GPIO.HIGH)
	time.sleep(0.01)
	GPIO.output(clock, GPIO.LOW)
	time.sleep(0.01)

GPIO.cleanup()




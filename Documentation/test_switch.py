import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(21,GPIO.OUT, initial = GPIO.LOW)

while 1==1:
	print "Select camera (A or B): "
	channel = raw_input()
	if channel == "A":
		GPIO.output(21,GPIO.LOW)
	elif channel == "B":
		GPIO.output(21,GPIO.HIGH)
	elif channel =="q":
		break
	else:
		print "Invalid selection"


GPIO.cleanup()

import vlc
import RPi.GPIO as GPIO
import time

prev_input = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

p = vlc.MediaPlayer("mp3_stream_here")
		
while True:
	input = GPIO.input(23)
	if ((not prev_input) and input):
		print("Switch Turned On")
		p.play()
	prev_input = input
	time.sleep(0.05)
	input = GPIO.input(23)
	if ((not prev_input) and input == 0):
		print("Switch Turned Off")
		p.stop()
		prev_input = input
		time.sleep(1)





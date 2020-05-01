import machine
import time

tPin = machine.Pin(17, machine.Pin.OUT)
ePin = machine.Pin(16, machine.Pin.IN)

def distance_in_cm():
	start = 0
	delta = 0	

	# Create a microseconds counter.

	tPin.off()
	time.sleep_us(5)

	# Send a 10us pulse.
	tPin.on()
	time.sleep_us(10)
	tPin.off()

	# Wait 'till whe pulse starts.
	while ePin.value() == 0:
		# start = micros.counter()
		start = time.ticks_us() # get millisecond counter)

	# Wait 'till the pulse is gone.
	while ePin.value() == 1:
		delta = time.ticks_diff(time.ticks_us(), start) # compute time difference

	dist_in_cm = (delta / 2) / 29

	return dist_in_cm

# function that prints each sensor's distance
def print_sensor_values():
	# get sensor1's distance in cm
	distance1 = distance_in_cm()
	print("Sensor1 (Metric System)", distance1, "cm")
 
# prints values every second

while (True):
    print_sensor_values()
    time.sleep_ms(200)
from sense_hat import SenseHat

sense = SenseHat()

X = [100,100,100]
O = [0,0,0]

inital_state = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

sense.set_pixels(inital_state)

dotx = 3
doty = 3

sense.set_pixel(dotx, doty, 150, 150, 150)

count = 0
while True:
	event = sense.stick.wait_for_event()
	
	dir = event.direction
	
	if event.action != "pressed":
		continue

	sense.set_pixel(dotx, doty, 0, 0, 0)
	
	if dir == "up":
		doty -= 1
	elif dir == "down":
		doty += 1
	elif dir == "right":
		dotx += 1
	elif dir == "left":
		dotx -= 1
	else:
		break
	
	sense.set_pixel(dotx, doty, 150, 150, 150)

sense.set_pixels(inital_state)

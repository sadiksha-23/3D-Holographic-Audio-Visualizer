# Importing the LED class from gpiozero to control an LED connected to a GPIO pin
from gpiozero import LED

# Importing the sleep function from time module to pause the program for a short time
from time import sleep

# Initialize the LED object connected to GPIO pin 18
led = LED(18)

# Turn the LED on (set the GPIO pin 18 to HIGH)
led.on()

# Pause the program for 0.1 seconds (LED stays on for a short time)
sleep(0.1)

# Turn the LED off (set the GPIO pin 18 to LOW)
led.off()
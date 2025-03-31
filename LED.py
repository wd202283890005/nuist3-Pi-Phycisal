# Import necessary libraries
import RPi.GPIO as GPIO  # Library for GPIO control
import time              # Library for time-related functions

# Set up GPIO mode and disable warnings
GPIO.setmode(GPIO.BCM)   # Use Broadcom SOC channel numbering (BCM)
GPIO.setwarnings(False)  # Disable runtime warning messages

# Configure GPIO pin 18 as output
GPIO.setup(18, GPIO.OUT) # Set GPIO18 as output pin

# Turn LED on
print("LED ON")                   # Print status to console
GPIO.output(18, GPIO.HIGH)        # Set pin to HIGH (3.3V) to turn LED on
time.sleep(1)                     # Keep LED on for 1 second

# Turn LED off
print("LED OFF")                  # Print status to console
GPIO.output(18, GPIO.LOW)         # Set pin to LOW (0V) to turn LED off



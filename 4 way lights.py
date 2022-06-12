# This code is for a 4 way direction uk traffic light for demonstration purposes written by John Holmes
# Date 31/5/22
# ---
# The code is written in MicroPpython
# And uses 2 libraries Machine, and utime
# machine gives us access to the GP input and output pins on the Pi Pico
# utime gives us access to the sleep function
# ---
# Connections used for the demonstration are
# BANK 1
# RED GP0, AMBER GP1, GREEN GP2
#
# BANK 2
# RED GP3, AMBER GP4, GREEN GP5
# 
# BANK 1A
# RED GP6, AMBER GP7, GREEN GP16
#
# BANK 2A
# RED GP28, AMBER GP27, GREEN GP26
# ---
# Hardware:
# 1. Cytron Maker Pi RP2040 (www.cytron.io/p-MAKER-PI-RP2040)
# - Any RP2040 boards should work too.
# ---

# Import the 2 library's
from machine import Pin
import utime

# Give meaning full variable names to the pins and set then up as outputs in this case
red1 = Pin(0,Pin.OUT)
amber1 = Pin(1,Pin.OUT)
green1 = Pin(2,Pin.OUT)

red2 = Pin(3,Pin.OUT)
amber2 = Pin(4,Pin.OUT)
green2 = Pin(5,Pin.OUT)

red1a = Pin(6,Pin.OUT)
amber1a = Pin(7,Pin.OUT)
green1a = Pin(16,Pin.OUT)

red2a =Pin(28,Pin.OUT)
amber2a = Pin(27,Pin.OUT)
green2a = Pin(26,Pin.OUT)


# Next i setup 6 functions to be used in the while loop of the program.
# When the function gets call it will run through 1 line at a time.
# Once the final line of code gets completed it will return back to the next line in the while loop.

def step1():
    red1.high()
    amber1.low()
    red1a.high()
    amber1a.low()
    red2.high()
    amber2.high()
    red2a.high()
    amber2a.high()
    utime.sleep(2)
   
def step2():
    red1.high()
    red1a.high()
    red2.low()
    amber2.low()
    green2.high()
    red2a.low()
    amber2a.low()
    green2a.high()
    utime.sleep(9)
    
def step3():
    red1.high()
    red1a.high()
    green2.low()
    amber2.high()
    green2a.low()
    amber2a.high()
    utime.sleep(2)
    
def step4():
    red1.high()
    amber1.high()
    red1a.high()
    amber1a.high()
    amber2.low()
    red2.high()
    amber2a.low()
    red2a.high()
    utime.sleep(2)
    
def step5():
    red1.low()
    amber1.low()
    green1.high()
    red1a.low()
    amber1a.low()
    green1a.high()
    red2.high()
    red2a.high()
    utime.sleep(15)
    
def step6():
    green1.low()
    amber1.high()
    green1a.low()
    amber1a.high()
    red2.high()
    red2a.high()
    utime.sleep(2)
 
# The while loop will run for ever will the Pi Pico has power.
# As we do not return anything to set it as false.
# You can see each of the functions gets called 1 line at a time.
# Once red_amber() function completes it will return to the top of the list.
while True:

    step1()
    step2()
    step3()
    step4()
    step5()
    step6()
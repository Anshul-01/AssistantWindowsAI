from json.tool import main
from tkinter.tix import MAIN
import pyfirmata
import time

comport = 'COM6'

board = pyfirmata.Arduino(comport)

led_1 = board.get_pin('d:13:o')
led_2 = board.get_pin('d:12:o')
led_3 = board.get_pin('d:11:o')
led_4 = board.get_pin('d:10:o')
led_5 = board.get_pin('d:9:o')
led_6 = board.get_pin('d:8:o')

def light(_arr):
    led_1.write(_arr[0])
    led_2.write(_arr[1])
    led_3.write(_arr[2])
    led_4.write(_arr[3])
    led_5.write(_arr[4])
    led_6.write(_arr[5])

def loopLed1():
    for i in range (0,54):
        arr = [0,0,0,0,0,0]
        j = i%6
        arr[j] = 1
        light(arr)
        time.sleep(0.1)

def loopLed2():
    for l in range(0,2):
        j=6
        arr = [0,0,0,0,0,0]
        while j >= 0:
            i=0
            while i<j :
                arr[i]=1
                light(arr)
                time.sleep(0.1)
                arr[i]=0
                i = i+1
            j = j-1
            arr[j] = 1
            
        # arr1 = [0,0,0,0,0,0]
        # light(arr1)

        j=0
        while j < 6 :
            i=0
            while i<=j:
                arr[i] = 1
                light(arr)
                time.sleep(0.1)
                arr[i] = 0
                i = i+1

            arr[j] = 0
            j = j+1
            
        light(arr)
#-------------------------------------------------------------------------------------------------
        i=-1
        arr = [0,0,0,0,0,0]
        while i < 5:
            j=5
            while i<j :
                arr[j]=1
                light(arr)
                time.sleep(0.1)
                arr[j]=0
                j = j-1
            i = i+1
            arr[i] = 1
            
        # arr1 = [0,0,0,0,0,0]
        # light(arr1)

        i=5
        while i>=0 :
            j=5
            while i<=j:
                arr[j] = 1
                light(arr)
                time.sleep(0.1)
                arr[j] = 0
                j = j-1

            arr[i] = 0
            i = i-1
            
        light(arr)
        
def loopNill():
    led_1.write(0)
    led_2.write(0)
    led_3.write(0)
    led_4.write(0)
    led_5.write(0)
    led_6.write(0)

def manualGlow(l1 ,l2 ,l3):
        led_1.write(l2)
        led_2.write(l1)
        led_3.write(l3)
        led_4.write(l2)
        led_5.write(l1)
        led_6.write(l3)
    
if __name__ == '__main__':
    # loopLed1()
    loopLed2()
    loopNill()


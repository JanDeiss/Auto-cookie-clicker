#new commit test

import mouse
import time
import keyboard
import os

enabled = True
click = mouse.click('left')
x = 200
y = 400

print("Press Q to cancel")

while(enabled == True):
 time.sleep(0.01)
 mouse.move(x,y)
 mouse.click()
 
 if keyboard.is_pressed('q'):
  os.system('cls' if os.name == 'nt' else 'clear')
  break

 




import pyautogui 
import time   

# Ensures the script doesn't fail when you have the mouse pointer in the top left corner
pyautogui.FAILSAFE = False  

# The `shift` key is a good key to press, but a different key may be selected (see https://pyautogui.readthedocs.io/en/latest/keyboard.html)
key = 'shift'

# Number of press repetitions
presses = 1

# Infinite loop
while 1:
    # Seconds between each press
    time.sleep(300)
    
    # Press the `key`
    pyautogui.press(keys=key, presses=presses) 

    # For informational purposes: this line prints, to the console, the time at which `key` is pressed 
    print(f"{key.title()} was pressed at {time.strftime('%I:%M:%S %p')}")

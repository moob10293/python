import pyautogui,time
from pynput import keyboard

pyautogui.FAILSAFE=True

try:
    click_speed=eval(input('how fast do you want your autoclicker to click? '))
except SyntaxError:
    click_speed=13

pyautogui.PAUSE=0
time.sleep(5)
'''

pyautogui.FAILSAFE=True

ht=eval(input('how long do you want the autoholder to press and hold?'))

if ht==0:
    ht=5
float(ht)

pyautogui.PAUSE=0.1

'''

doclickr = False
doclickl = False
def click(k):
    global doclickr
    global doclickl
    if k==keyboard.KeyCode(char=']'):
        doclickr = not doclickr
    if k == keyboard.KeyCode(char='['):
        doclickl = not doclickl
l=keyboard.Listener(on_press=click)
l.start()
while True:
    if doclickl:
        pyautogui.click(button="left")
        time.sleep(1/click_speed-0.001)
    if doclickr:
        pyautogui.click(button="right")
        time.sleep(1/click_speed-0.001)
input("")
while True:
    pyautogui.click()


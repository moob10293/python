import pyautogui, random
alphabet = []
for x in range(97,123):
    alphabet.append(chr(x))
for x in range(7):
    pyautogui.press(random.choice(alphabet))
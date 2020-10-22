import pyautogui, time
time.sleep(5)
f = open("venv/message", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("troll")

# fucking wit people spambot


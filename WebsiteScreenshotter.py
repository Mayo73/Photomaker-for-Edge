import pyautogui
import time

time.sleep(10)

#180 Mal für alle Seiten wiederholen
#for i in range(180):

# Startposition definieren
x_start = 500
y_start = 300

# Die Maus zur Zielposition bewegen
pyautogui.moveTo(x_start, y_start)

# Rechtsklick simulieren
pyautogui.rightClick()

# 12 Mal down drücken
pyautogui.press('down', presses=12)

# Enter drücken
pyautogui.press('enter', presses=1)

# Startposition des Fotos
startphoto_x = 881
startphoto_y = 137

# Die Maus zur Zielposition bewegen
pyautogui.moveTo(startphoto_x, startphoto_y)

# Die Maus zur Zielposition ziehen
pyautogui.dragTo(startphoto_x+753, startphoto_y+1071, duration=1)  # Duration ist die Zeit in Sekunden, die die Bewegung dauern soll

# Die Maus zur Zielposition bewegen
pyautogui.moveTo(1662, 1228)

# Linksklick simulieren
pyautogui.leftClick()

# Tastenkombination Alt + Tab ausführen (Programme wechseln (Zu Word wechseln))
pyautogui.hotkey('alt', 'tab')

# Tastenkombination Strg + V ausführen (Einfügen)
pyautogui.hotkey('ctrl', 'v')

# Tastenkombination Alt + Tab ausführen (Programme wechseln (Zur Website wechseln))
pyautogui.hotkey('alt', 'tab')

time.sleep(1)

# Die Maus zur Zielposition bewegen
pyautogui.moveTo(startphoto_x+738, 1200)

# Linksklick simulieren
pyautogui.leftClick()
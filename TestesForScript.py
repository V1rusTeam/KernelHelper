import pyautogui
from time import sleep

sleep(2)

a = pyautogui.locateCenterOnScreen("File.png")

if a == None:
    print("[-] File not found")
else:
    print("[+] File found!")

if a != None:
    x, y = pyautogui.locateCenterOnScreen("File.png")
    pyautogui.doubleClick(x, y)

sleep(10)

b = pyautogui.locateCenterOnScreen("clse.png")

if b == None:
    print("[-] Close not found")
else:
    print("[+] Close found!")

if b != None:
    x, y = pyautogui.locateCenterOnScreen("clse.png")
    pyautogui.click(x, y)

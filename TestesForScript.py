import pyautogui
from time import sleep

sleep(2)

a = pyautogui.locateCenterOnScreen("File.png")
b = pyautogui.locateCenterOnScreen("clse.png")

if a == None:
    print("[-] File not found")
else:
    print("[+] File found!")

if b == None:
    print("[-] Close not found")
else:
    print("[+] Close found!")
import pyautogui as auto
from time import sleep

while True:
    auto.write("hello")
    auto.press("enter")
    sleep(5)
import pyautogui
from pynput import keyboard
import os

def click_play_for_aegis():
    ori_pos = pyautogui.position()
    button_play_location = pyautogui.locateOnScreen(
        os.path.join('img','play_button.JPG'),
        confidence=0.7
    )
    click_pos_x = button_play_location.left+int(button_play_location.width/2)
    click_pos_y = button_play_location.top+int(button_play_location.height/2)
    pyautogui.click(click_pos_x,click_pos_y)
    pyautogui.moveTo(ori_pos.x,ori_pos.y)

def on_activate_p():
    click_play_for_aegis()

with keyboard.GlobalHotKeys({'<ctrl>+p':on_activate_p}) as h:
    h.join()
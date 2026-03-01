# action_controller.py

import pyautogui
import time
import config

class ActionController:
    def __init__(self):
        self.last_scroll_time = 0
        self.last_page_time = 0
        self.last_zoom_time = 0

    def zoom_in(self):
        if time.time() - self.last_zoom_time > config.ZOOM_COOLDOWN:
            pyautogui.hotkey('ctrl', '+')
            self.last_zoom_time = time.time()
            print("Zoom In")

    def zoom_out(self):
        if time.time() - self.last_zoom_time > config.ZOOM_COOLDOWN:
            pyautogui.hotkey('ctrl', '-')
            self.last_zoom_time = time.time()
            print("Zoom Out")

    def scroll_small_up(self):
        if time.time() - self.last_scroll_time > config.SCROLL_COOLDOWN:
            pyautogui.scroll(config.SMALL_SCROLL_AMOUNT)
            self.last_scroll_time = time.time()
            print("Scroll Up (Small)")

    def scroll_small_down(self):
        if time.time() - self.last_scroll_time > config.SCROLL_COOLDOWN:
            pyautogui.scroll(-config.SMALL_SCROLL_AMOUNT)
            self.last_scroll_time = time.time()
            print("Scroll Down (Small)")

    def scroll_large_up(self):
        if time.time() - self.last_page_time > config.PAGE_COOLDOWN:
            pyautogui.press('pageup')
            self.last_page_time = time.time()
            print("Page Up")

    def scroll_large_down(self):
        if time.time() - self.last_page_time > config.PAGE_COOLDOWN:
            pyautogui.press('pagedown')
            self.last_page_time = time.time()
            print("Page Down")

    def pan_left(self):
        pyautogui.hscroll(-20)
        print("Pan Left")

    def pan_right(self):
        pyautogui.hscroll(20)
        print("Pan Right")

    def dynamic_scroll(self, amount):
        pyautogui.scroll(-amount)
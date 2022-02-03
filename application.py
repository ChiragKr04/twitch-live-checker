import autoit
import time
from autoit import properties
from config import chrome_path, custom_message


def open_chrome(url: str):
    autoit.run(chrome_path, show_flag=3)
    autoit.win_wait_active("New Tab", timeout=10)
    left, top, right, bottom = autoit.win_get_pos('New Tab - Google Chrome')
    print(left, top, right, bottom)
    autoit.opt("SendKeyDelay", 10)
    autoit.send(f"!d{url}")
    time.sleep(0.1)
    autoit.send("{ENTER}")

    # moving mouse to maximize screen
    autoit.mouse_move(int(right - right * 0.04), int(top + top*0.15))
    # autoit.mouse_click()

    # moving mouse to twitch chat text field
    autoit.mouse_move(right, bottom)
    autoit.mouse_move(int(right - right * 0.1), int(bottom - bottom*0.07))
    time.sleep(10)
    autoit.mouse_click()
    autoit.opt("SendKeyDelay", 100)
    autoit.send(f"{custom_message}")
    autoit.send("{ENTER}")



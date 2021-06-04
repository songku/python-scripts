# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

import requests
import os
from selenium.webdriver import Chrome
import time
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = Chrome()
    driver.get("http://localhost/DVWA/login.php")
    time.sleep(10)  # 在这10s内你要人工登录
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

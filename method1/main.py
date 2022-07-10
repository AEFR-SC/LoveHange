"""
HangeKiller Beta-v0.1.0(Basic Functions)
@author: Versed_Sine (AEFR-SC)
@time: 2022/6/29 Midnight (23:25)
@mail: apesc1116@outlook.com

It is just a process listener,
when it heard the process that you want to kill,
it will just kill it.
There is a loop, so whatever the others do is just nothing for this file.
(Unless they kill this process.)
Some parts of the code is just from:
- CSDN user: "coordinate_blog" <https://coordinate.blog.csdn.net/?type=blog>,
    passage <https://blog.csdn.net/qq_17550379/article/details/79006718>;

Thanks to all of the "Code Providers"!
"""
# -*- coding: utf-8 -*-
from __future__ import print_function

import ctypes
import os
import sys
import pyautogui as ptg
import time

if sys.version_info[0] == 3:
    import winreg as winreg
else:
    import _winreg as winreg

CMD = r"C:\Windows\System32\cmd.exe"
FOD_HELPER = r'C:\Windows\System32\fodhelper.exe'
PYTHON_CMD = "python"
REG_PATH = 'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'


def is_admin():
    '''
    Checks if the script is running with administrative privileges.
    Returns True if is running as admin, False otherwise.
    '''
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def create_reg_key(key, value):
    '''
    Creates a reg key
    '''
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, key, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
    except WindowsError:
        raise


def bypass_uac(cmd):
    '''
    Tries to bypass the UAC
    '''
    try:
        create_reg_key(DELEGATE_EXEC_REG_KEY, '')
        create_reg_key(None, cmd)
    except WindowsError:
        raise


def execute():
    if not is_admin():
        print('[!] The script is NOT running with administrative privileges')
        print('[+] Trying to bypass the UAC')
        try:
            current_dir = __file__
            cmd = '{} /k {} {}'.format(CMD, PYTHON_CMD, current_dir)
            # r"C:\Windows\System32\cmd.exe /k python "+__file__
            # bypass_uac(cmd)
            os.system(FOD_HELPER)

            # print("exit0")
            # ptg.typewrite("taskkill /F /IM MicrosoftEdgeCP.exe")
            # ptg.press("enter")
            # print("Final to enter with ptg.")
            sys.exit(0)
        except WindowsError:
            sys.exit(1)
    else:
        # 这里添加我们需要管理员权限的代码
        print('[+] The script is running with administrative privileges!')
        while True:
            listen_to_the_browser()
            with open("D:\\ProcessList_Edge.txt", mode="r", encoding="utf-8") as killer:
                f = killer.readlines()
            list_of_processes = []
            for every_ in f:
                e = every_.split(" ")
                list_of_processes.append(e[0])
            for will_be_killed_process in list_of_processes:
                command = "taskkill /F /IM " + will_be_killed_process
                os.system(command)
        # os.system("Taskkill /fi \"pid ge 1\" /f")
        # input()


if __name__ == '__main__':
    execute()
    try:
        os.system(CMD)
    except ValueError as E:
        print(E)
    finally:
        print("Err catching done.")


def listen_to_the_browser(name="MicrosoftEdgeCP.exe"):
    commands = "tasklist|findstr -i " + name + " > D:\\ProcessList_Edge.txt"
    os.system(commands)

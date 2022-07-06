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
"""
from __future__ import print_function
import ctypes
import sys
import os


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def listen_to_the_browser(name="MicrosoftEdgeCP.exe"):
    commands = "tasklist|findstr -i " + name + " > D:\\ProcessList_Edge.txt"
    os.system(commands)


if __name__ == '__main__':
    if is_admin():  # 将要运行的代码加到这里
        print("已获取管理员权限...")
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

    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            print("run again...")
        else:
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
    input()

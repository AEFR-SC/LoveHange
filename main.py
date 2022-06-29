"""
HangeKiller Beta-v0.0.1(Basic Functions)
@author: Versed_Sine (AEFR-SC)
@time: 2022/6/29 Midnight (23:25)
@mail: apesc1116@outlook.com

It is just a process listener,
when it heard the process that you want to kill,
it will just kill it.
There is a loop, so whatever the others do is just nothing for this file.
(Unless they kill this process.)
"""
import os


def listen_to_the_browser(name="chrome.exe"):
    commands = "tasklist|findstr -i " + name + " > D:\\ProcessList_Edge.txt"
    os.system(commands)


if __name__ == '__main__':
    while True:
        listen_to_the_browser()
        with open("D:\\ProcessList_Edge.txt", mode="r", encoding="utf-8") as killer:
            f = killer.readlines()
        list_of_processes = []
        for every_ in f:
            e = every_.split(" ")
            list_of_processes.append(e[0])
        for will_be_killed_process in list_of_processes:
            command = "taskkill /F /IM "+will_be_killed_process
            os.system(command)

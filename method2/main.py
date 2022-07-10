# !/usr/bin/python3
# coding: utf-8
import os
import subprocess
import traceback


def runAdmin(cmd, timeout=1800000):
    f = None
    try:
        bat = os.getcwd() + r".\cmd.bat"
        f = open(bat, 'w')
        f.write(cmd)
    except Exception as e:
        traceback.print_exc()
        raise e
    finally:
        if f:
            f.close()

    try:
        shell = os.getcwd() + r".\shell.vbs"
        sp = subprocess.Popen(
            shell,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("[PID] %s: %s" % (sp.pid, cmd))
        sp.wait(timeout=timeout)

        stderr = str(sp.stderr.read().decode("gbk")).strip()
        stdout = str(sp.stdout.read().decode("gbk")).strip()
        if "" != stderr:
            raise Exception(stderr)
        if stdout.find("失败") > -1:
            raise Exception(stdout)
    except Exception as e:
        raise e


if __name__ == '__main__':
    runAdmin("taskkill /F /IM morgen.exe")

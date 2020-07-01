# coding:utf-8
import os
import time
import random
#home按键位置120 2171
#点赞 980 1250
#评论  980 1490
adbShell = "adb shell  {cmdStr}"


def execute(cmd):
    str = adbShell.format(cmdStr=cmd)
    print(str)
    os.system(str)

def next():
    x1 = str(random.randint(500, 550))
    y1 = str(random.randint(1600, 1800))
    x2 = str(random.randint(700, 750))
    y2 = str(random.randint(900, 1100))
    time = str(random.randint(50, 100))
    execute("input swipe " + x1 + ' ' + y1 + ' ' + x2 + ' ' + y2 + ' ' + time)  # 滑动

def like():
    execute("input tap 1000 1200")  # 点赞

def refrash():
    execute("input tap 120 2171")  # 点赞

if __name__ == '__main__':
    while True:
        next()
        temp_time = random.randint(3,15)
        time.sleep(temp_time)
        if temp_time > 10:
            like()
            time.sleep(1)
        elif temp_time == 14:
            refrash()
            time.sleep(3)


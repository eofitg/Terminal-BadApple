#!/usr/bin/env python3
import os

import cv2

import graying
import binarization
import characterization

video_path = 'input/video/'


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def img_apple(str):
    graying.Gary(str)  # 灰度化
    binarization.Bin()  # 二值化
    characterization.Cha()  # 字符化


def apple_str(str):
    return characterization.cha(str)


def apple_img(img):
    return characterization.img_cha(img)


def vid_apple(vid):
    vid = cv2.VideoCapture(video_path + vid)
    ret, frame = vid.read()
    while ret:
        # os.system('cls')
        s = apple_img(frame)
        print(s)
        ret, frame = vid.read()
        # cv2.waitKey(1)
        # 6573 frames


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # s = 'test.jpeg'
    # Img_Apple(s)

    # s = 'BadApple.jpg'
    # print(apple_str(s))

    video = 'BadApple.mp4'
    vid_apple(video)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import cv2

import binarization

input_path = 'output/image/binarization/'
output_path = 'output/image/characterization/'


def Cha():
    f = open(output_path + 'CharApple.txt', 'w')
    im = cv2.imread(input_path + 'BinaryApple.jpg')
    w = im.shape[1]
    h = im.shape[0]
    im = cv2.resize(im, (192 * 2, 81 * 2))
    # 512 384
    str = ""
    for i in im:
        for j in i:
            if j[0] == 0:
                str += '.'
            else:
                str += '@'
        str += '\n'
    f.write(str)
    f.close()


def cha(str):
    im = binarization.bin(str)
    im = cv2.resize(im, (192 * 3, 81 * 2))
    res = ""
    for i in im:
        for j in i:
            if j == 0:
                res += '.'
            else:
                res += '@'
        res += '\n'
    return res


def img_cha(im):
    im = cv2.resize(binarization.img_bin(im), (175 * 3, 88 * 2))
    res = ""
    for i in im:
        for j in i:
            if j == 0:
                res += '.'
            else:
                res += '@'
        res += '\n'
    return res


'''

f = open(output_path + 'CharApple.txt', 'w')

im = cv2.imread(input_path + 'BinaryApple.jpg')
im = cv2.resize(im, (192 * 2, 120 * 2))

str = ""

for i in im:
    for j in i:
        if j[0] == 0:
            str += '.'
        else:
            str += '@'
    str += '\n'

f.write(str)
f.close()

'''

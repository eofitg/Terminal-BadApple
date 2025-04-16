import cv2

import graying

input_path = 'output/image/graying/'
output_path = 'output/image/binarization/'


def Bin():
    im = cv2.imread(input_path + 'GrayApple.jpg')
    ret, binary = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(output_path + "BinaryApple.jpg", binary)


def bin(str):
    im = graying.gray(str)
    ret, binary = cv2.threshold(im, 127, 225, cv2.THRESH_BINARY)
    return binary


def img_bin(im):
    ret, binary = cv2.threshold(graying.img_gray(im), 127, 225, cv2.THRESH_BINARY)
    return binary


'''

im = cv2.imread(input_path + 'GrayApple.jpg')

ret, binary = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Bad Apple', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(output_path + "BinaryApple.jpg", binary)

'''

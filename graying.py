import cv2

input_path = 'input/image/'
output_path = 'output/image/graying/'


def Gary(str):
    im = cv2.imread(input_path + str)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path + "GrayApple.jpg", gray)


def gray(str):
    im = cv2.imread(input_path + str)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    return gray


def img_gray(im):
    return cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)


'''

im = cv2.imread(input_path + 'BadApple.jpg')

cv2.imshow('im', im)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

cv2.imshow('Bad Apple', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(output_path + "GrayApple.jpg", gray)

'''

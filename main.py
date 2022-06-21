import time

import pygame as pygame

from Interface import *
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

# img = mpimg.imread('moon.jpg')
# img2 = mpimg.imread('mouette.jpg')
fleche = mpimg.imread('fleche.png')
img1 = mpimg.imread('IMG_1.jpg')
img2 = mpimg.imread('IMG_2.jpg')
img3 = mpimg.imread('IMG_3.jpg')

# red = np.array([[[255, 0, 0]] * img.shape[1]] * img.shape[0])
# green = np.array([[[0, 255, 0]] * img.shape[1]] * img.shape[0])
# blue = np.array([[[0, 0, 255]] * img.shape[1]] * img.shape[0])


def moy_img(img):
    moy = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            moy += (img[i][j][0] + img[i][j][1] + img[i][j][2]) / 3
    moy /= (img.shape[0] * img.shape[1])
    return moy


def truc(img, n):
    if img.shape[0] * img.shape[1] == 0:
        return 0
    moy = 0
    print(img.shape)
    for i in range(-1 * img.shape[0] // 2, img.shape[0] // 2):
        for j in range(-1 * img.shape[1] // 2, img.shape[1] // 2):
            r = 1
            if not (i == 0 and j == 0):
                r = 1 - 1 / (2 * (abs(i) + abs(j)))
            moy += img[i][j][n] * r
    moy /= (img.shape[0] * img.shape[1])
    return moy


def moy_ind(img, x):
    if img.shape[0] * img.shape[1] == 0:
        return 0
    n = min(img.shape[0], img.shape[1])
    moy = 0
    s = 0
    if n % 2 == 1:
        l = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if not (i - 1 * n // 2 == 0 and j - 1 * n // 2 == 0):
                    r = 1 / (2 * abs(i - 1 * n // 2) + 2 * abs(j - 1 * n // 2))
                else:
                    r = 1
                l[i][j] = r
            s += sum(l[i])
    else:
        l = np.zeros((n + 1, n + 1))
        for i in range(n + 1):
            for j in range(n + 1):
                if not ((i - 1 * n // 2 == 0) or (j - 1 * n // 2 == 0)):
                    r = 1 / (abs(i - 1 * n // 2) + abs(j - 1 * n // 2))
                    l[i][j] = r
            if not ((i - 1 * n // 2 == 0) or (j - 1 * n // 2 == 0)):
                s += sum(l[i])
        l = np.delete(np.delete(l, np.s_[l.shape[0] // 2], 1), l.shape[0] // 2, 0)
    # print(img.shape)
    for i in range(n):
        for j in range(n):
            # print(img,'------',l)
            moy += img[i][j][x] * l[i][j]
    moy /= s
    return moy


# double for loop to create a new image
def mean(img, img2):
    new_img = np.zeros((img.shape[0], img.shape[1], 3))
    coeff = 0.01
    coeff2 = 1
    moy = moy_img(img)
    moy2 = moy_img(img2)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            new_img[i][j] = [(coeff * int((img[i][j][0] + coeff2 * img2[i][j][0])) * moy2 / moy),
                             (coeff * int((img[i][j][1] + coeff2 * img2[i][j][1])) * moy2 / moy),
                             (coeff * int((img[i][j][2] + coeff2 * img2[i][j][2])) * moy2 / moy)]

    return new_img


def mean3(img, img2, img3):
    new_img = np.zeros((img.shape[0], img.shape[1], 3))
    coeff = 1
    coeff2 = 1
    coeff3 = 1
    moy = moy_img(img)
    moy2 = moy_img(img2)
    moy3 = moy_img(img3)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            new_img[i][j] = [
                (coeff * int((img[i][j][0] + coeff2 * img2[i][j][0] + coeff3 * img3[i][j][0])) * moy3 / (moy2 * moy)),
                (coeff * int((img[i][j][1] + coeff2 * img2[i][j][1] + coeff3 * img3[i][j][1])) * moy3 / (moy2 * moy)),
                (coeff * int((img[i][j][2] + coeff2 * img2[i][j][2] + coeff3 * img3[i][j][2])) * moy3 / (moy2 * moy))]

    return new_img


# write a method to resize the image
def resize(img, new_shape):
    new_img = np.zeros((new_shape[0], new_shape[1], 3))
    ratio = new_shape[0] / img.shape[0]
    ratio = 1 / ratio
    print(ratio)
    for i in range(new_shape[0]):
        for j in range(new_shape[1]):
            a, b, c, d = int(i * ratio), int(j * ratio), int((i + 1) * ratio), int((j + 1) * ratio)
            if a >= img.shape[0] - 1:
                break
            if b >= img.shape[1] - 1:
                break
            if c >= img.shape[0] - 1:
                break
            if d >= img.shape[1] - 1:
                break
            x, y = int(i * ratio), int(j * ratio)
            if x >= img.shape[0] - 1:
                break
            if y >= img.shape[1] - 1:
                break
            moy0 = moy_ind(img[a:c, b:d], 0)
            if moy0 == 0:
                moy0 = img[x, y][0]
            moy1 = moy_ind(img[a:c, b:d], 1)
            if moy1 == 0:
                moy1 = img[x, y][1]
            moy2 = moy_ind(img[a:c, b:d], 2)
            if moy2 == 0:
                moy2 = img[x, y][2]
            new_img[i][j] = [moy0 / 255, moy1 / 255, moy2 / 255]
    new_img = np.delete(new_img, np.s_[int(img.shape[1] / ratio):], axis=1)
    return new_img


def rotate(img, angle):
    new_img = ndimage.rotate(img, angle, reshape=False)
    return new_img


half1 = (img1.shape[0] // 2, img1.shape[1] // 2, 3)
# quarter = (img.shape[0] // 4, img.shape[1] // 4, 3)
# double = (img.shape[0] * 2, img.shape[1] * 2, 3)
# quad = (img.shape[0] * 4, img.shape[1] * 4, 3)
# oct = (img.shape[0] * 8, img.shape[1] * 8, 3)

# variable containing the current time
# t = time.time()
# new_img = resize(img, oct)
# plt.imshow(rotate(fleche,90))
# plt.show()
# # plt.imshow(new_img)
# img35 = rotate(mpimg.imread('img34.jpg'), 358)
# plt.imsave('img35.jpg', img35)
# plt.imshow(img35)
# plt.show()

if __name__ == '__main__':
    while True:
        menu = Interface('img15.jpg')
        pygame.display.flip()  # Actualise lecran
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # quit game if a click collide the elipse button at [taille_ecran_menu[1] // 2, 350, 300, 100]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    event_pos = pygame.mouse.get_pos()
                    print(event_pos)

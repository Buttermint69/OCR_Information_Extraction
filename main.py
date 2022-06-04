# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib
import tesserocr as tes
import cv2 as cv
import funcs
from funcs import pre_process
from Information_extraxion import regex
from functools import reduce

img = cv.imread("img.png")
blur, thres, ed = pre_process(img)


def print_hi(txt):
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.
    c = regex()
    print(c.info_extract(txt))


def item_extraction(txt):

    l = txt.split('\n')
    txt2 = []

    for idx, i in enumerate(l):
        if reduce((lambda x, y: x or y), list(map(lambda x: True if (x == "Amt") else False, i.split(" ")))):
            for j in range(idx + 1, len(l)):
                if reduce((lambda x, y: x or y),
                          list(map(lambda x: True if (x == "Total") else False, l[j].split(" ")))):
                    break
                else:
                    txt2.append(l[j])
    return txt2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    text, bbox = funcs.text_extraction(ed)
    print_hi(text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
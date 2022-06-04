import cv2 as cv
import numpy as np
import tesserocr as tes
from tesserocr import PyTessBaseAPI, RIL, PSM, OEM
import os


def pre_process(img, level=3):
    """
    :param img: cv2 image object
    :param level: pre-processing level;
    :return: if 0 only blured image will return;
             if 1 binary threshold image;
             if 2 eroded - dilated image;
             if 3 all three kinds will return
    """

    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    blur_img = cv.medianBlur(img_rgb, 5, cv.BORDER_DEFAULT)
    thres = cv.threshold(img_rgb, 195, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

    kernel = np.ones((3, 3), np.uint8)
    img = cv.morphologyEx(thres, cv.MORPH_OPEN, kernel)

    if level == 0:
        return blur_img
    elif level == 1:
        return thres
    elif level == 2:
        return img
    elif level == 3:
        return blur_img, thres, img


def text_extraction(img, psm=6, oem=3):
    """
    :param img: cv2 image object
    :param psm: page segmentation mode
    :param oem: tesseract ocr engine
    :return: text, bounding boxes
    """

    path = "C:/Users/Harshit/anaconda3/envs/major_proj/share/tessdata"
    cv.imwrite("im.png", img)
    text = tes.file_to_text("im.png", psm=psm, oem=oem, path=path)
    with PyTessBaseAPI(path=path, psm=6, oem=3) as api:
        level = RIL.WORD
        api.SetImageFile("im.png")
        api.Recognize()
        ri = api.GetIterator()
        box_2 = []
        while ri.Next(level):
            boxes = ri.BoundingBox(level)
            box_2.append(boxes)

    os.remove("im.png")
    return text, box_2
# OCR_Information_Extraction

Optical Character Recognition (OCR) with tesser-ocr for conversion of images of typed, handwritten or printed text into machine-encoded text. In this work the text conversion from an medicene bill reciept following with information extraction with regular expression matching.

Image - 
https://github.com/Buttermint69/OCR_Information_Extraction/blob/master/img.png
![image](https://user-images.githubusercontent.com/78033216/172024287-62057d87-8c85-477d-b965-74d51ecc3224.png)

The image is pre-processed with opencv tool for reducing the noise and amplifying the pixels. Various experimentations are performed and then selected the best technique [erosion-dilation] for the problem.

Extracted text bounding box -

![image](https://user-images.githubusercontent.com/78033216/172024365-d52e0d09-871b-4ccd-b393-983cb3802954.png)

Furthermore, the extracted text processing into pandas Dataframe object.

                                                                                                                      -- Harshit Tiwari

import cv2 as cv
import modules.getEnds as ends
import feature as feat
import termTrim as tt

img = cv.imread('test3.png')

blur = cv.blur(img, (5, 5))
gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)
 
cut = tt.trim(thresh, 5, 5, 5 ,5)
# cut = tt.trim(thresh)
cv.imwrite('out.png', cut)
akaze = feat.getAkaze(cut)

while True:
  cv.imshow('test', akaze)
  cv.waitKey(25)
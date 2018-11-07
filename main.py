import cv2 as cv
import modules.getEnds as ends
import feature as feat
import termTrim as tt

img = cv.imread('test2.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)

endLeft = ends.endLeft(thresh)
endRight = ends.endRight(thresh)
endTop = ends.endTop(thresh)
endBottom = ends.endBottom(thresh)

print(endBottom) 
 
cut = tt.trim(thresh, 5, 5, 5 ,5)
# cut = tt.trim(thresh)
cv.imwrite('out.png', cut)
akaze = feat.getAkaze(cut)

while True:
  cv.imshow('test', cut)
  cv.waitKey(25)
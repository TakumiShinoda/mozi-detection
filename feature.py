import cv2 as cv

def getAkaze(gray):
  akaze = cv.AKAZE_create()
  kp1 = akaze.detect(gray)
  result = cv.drawKeypoints(gray, kp1, None, flags=4)

  return result
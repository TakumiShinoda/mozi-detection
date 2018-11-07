import cv2 as cv

def getAkaze(gray):
  akaze = cv.AKAZE_create()
  kp, des = akaze.detectAndCompute(gray, None)
  result = cv.drawKeypoints(gray, kp, None, flags=4)

  return result, kp, des
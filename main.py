import cv2 as cv
import modules.getEnds as ends
import feature as feat
import termTrim as tt

def scale(img, width, height, keep_aspect=True):
  if keep_aspect:
    scale = max(width / img.shape[1], height / img.shape[0])
    return cv.resize(img, dsize=None, fx=scale, fy=scale)
  else:
    return cv.resize(img, (width, height))

def mainProc(img):
  blur = cv.blur(img, (10, 10))
  gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
  ret, thresh = cv.threshold(gray, 180, 255, cv.THRESH_BINARY)
  result = {}
  
  cut = tt.trim(thresh, 10, 10, 10, 10)
  cut = scale(cut, 200, 200, keep_aspect=False)
  result['original'] = cut
  cv.imwrite('out.png', cut)
  result['detectedImg'], result['kp'], result['des'] = feat.getAkaze(cut)

  return result

test1 = cv.imread('test.png')
test2 = cv.imread('test2.png')
test3 = cv.imread('test3.png')

res_test1 = mainProc(test1)
res_test2 = mainProc(test2)
res_test3 = mainProc(test3)

# //// matching by algorithm included opencv 
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches = bf.match(res_test1['des'], res_test3['des'])
matches = sorted(matches, key = lambda x:x.distance)
test1_test3 = cv.drawMatches(res_test1['original'], res_test1['kp'], res_test3['original'], res_test3['kp'], matches[:10], None, flags=2)
# test1_test2 = cv.drawMatches(res_test1['original'], res_test1['kp'], res_test2['original'], res_test2['kp'], matches[:10], None, flags=2)
# test2_test3 = cv.drawMatches(res_test2['original'], res_test2['kp'], res_test3['original'], res_test3['kp'], matches[:10], None, flags=2)

# //// matching by knn algorithm 
# bf = cv.BFMatcher()
# matches = bf.knnMatch(res_test1['des'], res_test2['des'], k=2)
# good = []
# for m,n in matches:
#   if m.distance < 0.5*n.distance:
#     good.append([m])
# test1_test2 = cv.drawMatchesKnn(res_test1['original'], res_test1['kp'], res_test2['original'], res_test2['kp'], good, None, flags=2)

while True:
  cv.imshow('test1', res_test1['detectedImg'])
  cv.imshow('test2', res_test2['detectedImg'])
  cv.imshow('test3', res_test3['detectedImg'])
  cv.imshow('1-3', test1_test3)
  # cv.imshow('1-2', test1_test2)
  # cv.imshow('2-3', test2_test3)
  cv.waitKey(25)
import cv2 as cv
import numpy as np
import modules.getEnds as ends

def trim(img, spaceLeft = 0, spaceTop = 0, spaceRight = 0, spaceBottom = 0):
  result = img
  width = result.shape[0]
  height = result.shape[1]
  allEnds = ends.getAll(result) 
  trimPos = np.array([0, 0, 0, 0])
 
  if(allEnds[0][0] - spaceLeft < 0):
    trimPos[0] = 0
  else:
    trimPos[0] = allEnds[0][0] - spaceLeft

  if(allEnds[1][1] - spaceTop < 0):
    trimPos[1] = 0
  else:
    trimPos[1] = allEnds[1][1] - spaceTop
  
  if(allEnds[2][0] + spaceRight >= width):
    trimPos[2] = 0
  else:
    trimPos[2] = allEnds[2][0] + spaceRight

  if(allEnds[3][1] + spaceBottom >= height):
    trimPos[3] = 0
  else:
    trimPos[3] = allEnds[3][1] + spaceLeft

  print(trimPos)

  result = result[trimPos[1]:trimPos[3], trimPos[0]:trimPos[2]] 

  return result
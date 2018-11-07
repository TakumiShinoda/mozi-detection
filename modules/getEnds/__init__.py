import numpy as np

def endLeft(img):
  result = np.array([0, 0])
  resX = 0
  resY = 0
  frag = False
  width = img.shape[1]
  height = img.shape[0]

  for w in range(width):
    for h in range(height):
      if(img[h][w] == 0):
        resX = w
        resY = h
        frag = True        
        break
    if(frag):
      break

  result[0] = resX
  result[1] = resY
  return result

def endRight(img):
  result = np.array([0, 0])
  resX = 0
  resY = 0
  frag = False
  width = img.shape[1]
  height = img.shape[0]

  for w in range(width):
    for h in range(height):
      if(img[h][width - w - 1] == 0):  
        resX = width - w - 1
        resY = h
        frag = True        
        break
    if(frag):
      break

  result[0] = resX
  result[1] = resY
  return result

def endTop(img):
  result = np.array([0, 0]) 
  resX = 0
  resY = 0
  frag = False
  width = img.shape[1]
  height = img.shape[0]

  for h in range(height):
    for w in range(width):
      if(img[h][w] == 0):  
        resX = w
        resY = h
        frag = True        
        break
    if(frag):
      break  

  result[0] = resX
  result[1] = resY
  return result

def endBottom(img):
  result = np.array([0, 0]) 
  resX = 0
  resY = 0
  frag = False
  width = img.shape[1]
  height = img.shape[0]

  for h in range(height): 
    for w in range(width):
      if(img[height - h - 1][w] == 0):  
        resX = w
        resY = height - h - 1
        frag = True        
        break
    if(frag):
      break  

  result[0] = resX
  result[1] = resY
  return result

def getAll(img): 
  return np.array([endLeft(img), endTop(img), endRight(img), endBottom(img)])
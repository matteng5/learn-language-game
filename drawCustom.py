##########
#
#  Submission 1
#  Matthew Eng
#  Nov. 19, 2022
#  Objective: Implementation of five functions

### Libraries ###
import cmpt120image
import random
### End of Libraries ###

### Functions ###
def recolorImage(img,color):
  height = len(img)
  width = len(img[0])
  newImg = cmpt120image.getBlackImage(width,height)

  wThreshold = 246

  for h in range(height):
    for w in range(width):
      r,g,b=img[h][w][0],img[h][w][1],img[h][w][2]

      if r>=wThreshold and g>=wThreshold and b>=wThreshold:
        newImg[h][w] = [255,255,255]
      else:
        newImg[h][w] = color
  
  return newImg

def minify(img):
  def avgRGB(pixels):
    r,g,b=0,0,0

    for pix in pixels:
      r+=pix[0]
      g+=pix[1]
      b+=pix[2]

    return [r/len(pixels),g/len(pixels),b/len(pixels)]

  height = len(img)
  width = len(img[0])
  newImg = cmpt120image.getWhiteImage(width//2,height//2)

  for h in range(0,height,2):
    for w in range(0,width,2):
      if (h+1) < height and (w+1) < width:
        p1 = img[h][w]
        p2 = img[h][w+1]
        p3 = img[h+1][w]
        p4 = img[h+1][w+1]
        pix = avgRGB([p1,p2,p3,p4])

      elif (h+1) == height and (w+1) == width:
        pix = img[h][w]

      elif (h+1) == height:
        p1 = img[h][w]
        p2 = img[h][w+1]
        pix = avgRGB([p1,p2])

      else:
        p1 = img[h+1][w]
        p2 = img[h+1][w+1]
        pix = avgRGB([p1,p2])
      newImg[h//2][w//2] = pix

  return newImg


def mirror(img):
  height = len(img)
  width = len(img[0])
  newImg = cmpt120image.getBlackImage(width,height)

  for h in range(height):
    for w in range(width):
      pix = img[h][w]
      newImg[h][width-w-1]=pix
  
  return newImg

def drawItem(canvas,img,row,col):

  height = len(img)
  width = len(img[0])

  wThreshold = 246

  for h in range(height):
    for w in range(width):
      r,g,b=img[h][w][0],img[h][w][1],img[h][w][2]

      if r<wThreshold and g<wThreshold and b<wThreshold:
        canvas[h+row][w+col] = img[h][w]
  
  return canvas

def distributeItems(canvas,img,n):

  imgH = len(img)
  imgW = len(img[0])

  for i in range(0,n):
    rowRandom = random.randint(0,len(canvas)-imgH)
    colRandom = random.randint(0,len(canvas[0])-imgW)

    drawItem(canvas,img,rowRandom,colRandom)
  
  return canvas

### End of Functions ###

### Main Code ###
img = cmpt120image.getImage("images/test.png")
cmpt120image.showImage(img)
input("...")

res = recolorImage(img,[0,255,0])
cmpt120image.showImage(res)
input("...")

res = mirror(img)
cmpt120image.showImage(res)
input("...")

cnv = cmpt120image.getWhiteImage(400,300)
# Canvas is modified directly

res = drawItem(cnv,img,20,40)
cmpt120image.showImage(res)
input("...")

cnv = cmpt120image.getWhiteImage(400,300)
#Establish new canvas
res = distributeItems(cnv,img,4)
cmpt120image.showImage(res)
input("...")

### End ###

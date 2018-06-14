# setup

def setup():
  global backgroundImage
  global cloudImage
  global sephirothImage
  global spriteX
  size(960,540)
  spriteX = 0
  backgroundImage = loadImage("midgar.png")
  cloudImage = loadImage("cloud.png")
  sephirothImage = loadImage("sephiroth.png")

def keyPressed():
    global spriteX
    if (key == CODED):
        if(keyCode == LEFT):
            spriteX = spriteX -2
        elif (keyCode == RIGHT):
            spriteX = spriteX + 2
	
def draw():
	global backgroundImage
	global cloudImage
	global sephirothImage
	global spriteX
 	background(backgroundImage)
 	image(cloudImage, 200, 400)
 	image(sephirothImage, 600, 400)
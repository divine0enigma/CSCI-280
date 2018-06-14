# setup

def setup():
  global backgroundImage
  global obamaImage
  global hillaryImage
  global trumpImage
  global paulImage
  global spriteX
  size(1200,675)
  backgroundImage = loadImage("stage.png")
  obamaImage = loadImage("obama.png")
  hillaryImage = loadImage("hillary.png")
  trumpImage = loadImage("trump.png")
  paulImage = loadImage("paul.png")

# def keyPressed():
    # global spriteX
    # if (key == CODED):
        # if(keyCode == LEFT):
            # spriteX = spriteX -2
        # elif (keyCode == RIGHT):
            # spriteX = spriteX + 2
	
def draw():
 	background(backgroundImage)
 	image(obamaImage, 200, 400)
 	image(hillaryImage, 450, 400)
	image(trumpImage, 700, 400)
	image(paulImage, 1000, 400)
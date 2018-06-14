GhostMonster class
  attributes
     color - "red","pink","cyan",or "orange"
     state - "flee" or "chase"
     direction - "left", "right", "up", "down"
     frameNumber - 0 or 1
     imageList - List of Processing images one for each distinct appearance
     posX - Pixel x-coordinate of this ghost
     posY - Pixel y-coordinate of this ghost
     targetX - Pixel x-coordinate of current target
     targetY - Pixel y-coordinate of current target

class GhostMonster:
    # default constructor
    # Set color to "red"
    # Set state to "chase"
    # Set direction to "left"
    # Set imageList to empty list
    # Set frameNumber to 0
    # Set position and target coordinates to (0,0)
    def __init__(self):
        self.color = "red"
        self.state = "chase"
        self.direction = "left"
        self.posX = 0
        self.posY = 0
        self.imageList = []
        self.frameNumber = 0
        self.targetX = 0
        self.targetY = 0

    # assigning constructor
    # Set color to given value expected to be "red","pink","cyan", or "orange"
    # Set state to given value expected to be "chase" or "flee"
    # Set direction given value expected to be "left" or "right"
    # Set position to given X,Y values
    # Set imageList to given list
    # Set frameNumber to 0
    # Set target to (0,0) - will call updateTarget
    def __init__(self, color, state, dir, posX, posY, spriteImageList):
        self.color = color
        self.state = state
        self.direction = dir
        self.posX = posX
        self.posY = posY
        self.imageList = spriteImageList
        self.frameNumber = 0
        self.targetX = 0
        self.targetY = 0

    # setState - receives argument "chase" or "flee" and updates
    # state only if argument value is "chase" or "flee"
    def setState(self, S):
        if(S == "chase" or S == "flee"):
            self.state = S

    # setDirection - receives argument "left","right","up",or "down"
    # updates direction attribute only if argument value is "left" or "right"
    def setDirection(self, dir):
        if(dir == "left" or dir == "right" or dir == "up" or dir == "down"):
            self.direction = dir

    # updateTarget
    # Updates coordinates of target position after
    # ghost monster has changed state.
    # pre-condition: Receives reference to PacMan object
    # ghost knows position and direction of player.
    # Assume PacMan object has methods getPosX(), getPosY(),
    # getDirection(), and isPowerUp().
    # Receives Maze object that describes size of maze.
    def updateTarget(self, player, maze):
        # Use if-elif statement to call specialized target methods.
        # Convert pseudo code into statements

        if state is chase
           if ghost is red
              self.updateTargetRed
           else if ghost is pink
              call updateTargetPink
           else
              call updateTargetWander for less aggressive ghosts
        else if state is flee
           call updateTargetFlee

    # Updates coordinates of target position after
    # red ghost monster has changed state to chase
    # pre-condition: Receives reference to PacMan object
    def updateTargetRed(self, player):
        # Red ghost will make its target the current player position.

    # Updates coordinates of target position after
    # pink ghost monster has changed state to chase
    # pre-condition: Receives reference to PacMan object and
    # Receives Maze object that describes size of maze.
    # Assume Maze object has method getTilePixelSize()
    def updateTargetPink(self, player, maze):
        # Pink ghost will make its target 4 tiles ahead of
        # current player position.
        # Access player's direction using player's getDirection method.
        # Compute target position to be 4 tiles ahead of player position.
        # Convert 4 tiles into equivalent pixels by calling Maze's
        # getTilePixelSize() method.

    def wander(self, maze):
	# Roll a random integer 1,2,3,or 4
        # Assign direction of movement based on that roll.
        # Of course, the finished version must consider passable maze directions.

    def flee(self, maze):
        # Call on maze object's getGhostFleePositionX, getGhostFleePositionY
        # methods to set target depending on color of ghost.
        # getGhostFleePositionX and getGhostFleePositionY each receive
        # the color of a ghost and return its hiding corner coordinates.


    # animateFrame
    # increments frameNumber by 1.  Resets to 0 if exceeds 1.
    # More fancy version would receive elapsedTime for precise frame change timing.
    def animateFrame(self, player, maze):
        self.frameNumber = self.frameNumber + 1
        if (self.frameNumber > 1):
            self.frameNumber = 0

        # Move ghost in current direction

        # Check if any change of state events happen
        # update state of ghost
        # update ghost target position

    # getImage
    # receives nothing
    # Use state, direction, and frameNumber to compute the
    # integer list index to select the appropriate Processing image from imageList
    # return one Processing Image sprite from imageList
    def getImage(self):
        index = 0
        if (self.state == "chase"):
            if (self.direction == "left"):
                index = 0
            elif (self.direction == "right"):
                index = 2
        elif (self.state == "flee"):
            index = 4
        index = index + self.frameNumber
        return self.imageList[index]

def setup():
    global ghost

    # create list of sprite images
    imageList = []

    # Open PyProcessing graphics window with given width x height in pixels.
    size(320,320)

    # List of sprite file names.
    # Confirm these images are in your Sketch folder and filenames are correct.
    imageNameList = [ "ghost_chase_left_1.png", "ghost_chase_left_2.png",
                    "ghost_chase_right_1.png", "ghost_chase_right_2.png",
                    "ghost_flee_1.png", "ghost_flee_2.png" ]

    # Loop over list of image names, loading each image, and adding to imageList.
    for fname in imageNameList:
        print("Loading image ", fname)
        img = loadImage(fname)
        imageList.append(img)

    # Create a GhostMonster setting its initial state and list of images.
    ghost = GhostMonster("chase","left",imageList)

    # Set slow animation frame rate so we can see what is happening.
    frameRate(2)

def keyPressed():
    global ghost

    # For testing - keyboard press will change ghost state.
    if (key == CODED):
        if (keyCode == LEFT):
            ghost.setDirection("left")
        elif (keyCode == RIGHT):
            ghost.setDirection("right")
    elif (key == 'c' or key == 'C'):
        ghost.setState("chase")
    elif (key == 'f' or key == 'F'):
        ghost.setState("flee")

def draw():
    global ghost

    # Clear window to background color white
    background(255)

    # Get current image of ghost
    img = ghost.getImage()

    # Draw current image in center of window.
    image(img, 160,160)

    # Advance to next frame of animation.
    ghost.animateFrame()

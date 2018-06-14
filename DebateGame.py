import time
import sys

lockdown = 0
player1 = "Waiting"
player2 = "Waiting"

class Player:
    global lockdown
    def __init__(self):
        self.playerNumber = ""
        self.score = 50
        self.expression = "neutral"
        self.locked = False
        self.queue = 0
        self.move = 0

    def __init__(self, playerNumber, score, expression, locked, queue, move):
        self.playerNumber = playerNumber
        self.score = score
        self.expression = expression
        self.locked = locked
        self.queue = queue
        self.move = move

    def setExpression(self, E):
        if(self.expression == "neutral" or self.expression == "happy" or self.expression == "sad" or self.expression == "angry"):
            self.expression = E

    def getPlayerNumber(self):
        return self.playerNumber

    def setLocked(self, S):
        global lockdown
        self.locked = S

        if (self.locked != 0):
            if (lockdown == 1):
                self.setQueue(2)
            else:
                self.setQueue(1)
                lockdown = 1

    def getLocked(self):
        return self.locked

    def getScore(self):
        return self.score

    def setScore(self, S):
        # global debug
        # debug = "setScore"
        self.score = S
        if(self.score >= 100):
            endGame(self.getPlayerNumber(), "win")
        elif(self.score <= 0):
            endGame(self.getPlayerNumber(), "lose")

    def getQueue(self):
        return self.queue

    def setQueue(self, position):
        self.queue = position

    def getMove(self):
        # global debug
        # debug = self.move
        return self.move

    def setMove(self, M):
        # global debug
        # debug = M
        self.move = M

def roundReset(player1, player2):
    global lockdown
    # global debug
    lockdown = 0
    player1.setLocked(False)
    player1.setMove(0)
    player1.setQueue(0)
    player2.setLocked(False)
    player2.setMove(0)
    player2.setQueue(0)

def updateScore(player, value):
    # global debug
    # debug = value
    if(player.getPlayerNumber == 1):
        player1 = value
    else:
        player2 = value
    score = player.getScore()
    score += value
    player.setScore(score)

def roundResult(player1, player2):
    global debug
    ## Both Non Attack Move ##
    if (player1.getMove() <= 3 and player2.getMove() <= 3):
        ## Same Basic Move##
        if (player1.getMove() == player2.getMove()):
            flip = 0
            if(player2.getQueue() == 1):
                # debug = "flip"
                temp = player1
                player1 = player2
                player2 = temp
                flip = 1
            updateScore(player2, player2.getMove() * 2 + 1)
            updateScore(player1, player1.getMove() * 5 + 1)
            if(flip == 1):
               # debug = "reset"
                player2 = player1
                player1 = temp
                flip = 0;
            roundReset(player1, player2)
        ## Different Basic Move ##
        else:
            flip = 0
            if(player2.getQueue() == 1):
                temp = player1
                player1 = player2
                player2 = temp
                flip = 1
            updateScore(player1, player1.getMove() * 2 + 1)
            updateScore(player2, player2.getMove() * 2 + 1)
            if(flip == 1):
                player2 = player1
                player1 = temp
            roundReset(player1, player2)

    ## Player 2 Attack s##
    elif (player1.getMove() <= 3):
        ## Player 2 Critical Attack ##
        if (player2.getMove() - player1.getMove() == 3):
            updateScore(player1, (player1.getMove() * 2 + 1))
            updateScore(player2, (player1.getMove() * 2 + 2))
            updateScore(player1, (player1.getMove() * -4 -2))
            roundReset(player1, player2)
        ## Player 1 Counter Attack ##
        elif (player2.getMove() - player1.getMove() == 4):
            updateScore(player1, (player1.getMove() * 2 + 1))
            updateScore(player2, (player1.getMove() * - 5 -2))
            updateScore(player1, (player2.getMove() * 2 + 2))
            roundReset(player1, player2)
        ## Player 2 Basic Attack ##
        else:
            updateScore(player1, (player1.getMove() * 2 + 1))
            updateScore(player1, (player2.getMove() * -1 + 1))
            roundReset(player1, player2)

    ## Player 1 Attack ##

    elif(player2.getMove() <= 3):
        ## Player 1 Critical Attack ##
        if (player1.getMove() - player2.getMove() == 3):
            updateScore(player2, (player2.getMove() * 2 + 1))
            updateScore(player1, (player2.getMove() * 2 + 2))
            updateScore(player2, (player2.getMove() * -4 -2))
            roundReset(player1, player2)
        ## Player 2 Counter Attack ##
        elif (player1.getMove() - player2.getMove() == 4):
            updateScore(player2, (player2.getMove() * 2 + 1))
            updateScore(player1, (player2.getMove() * - 5 -2))
            updateScore(player2, (player1.getMove() * 2 + 2))
            roundReset(player1, player2)
        ## Player 1 Basic Attack ##
        else:
            updateScore(player2, (player2.getMove() * 2 + 1))
            updateScore(player2, (player1.getMove() * -1 + 1))
            roundReset(player1, player2)

    ## Players Basic Attack Eachother ##
    else:
        flip = 0
        if(player2.getQueue() == 1):
            temp = player1
            player1 = player2
            player2 = temp
            flip = 1
        updateScore(player2, (player1.getMove() * -1 + 1))
        updateScore(player1, (player2.getMove() * -1 + 1))
        if(flip == 1):
            player2 = player1
            player1 = temp
        roundReset(player1, player2)

def endGame(player, status):
    if(status == "win"):
        print("Player ", player, " wins")
        sys.exit()
    print("Player ", player, " loses")
    sys.exit()


# setup

def setup():
    global Player1
    global Player2
    global backgroundImage
    global hillaryImage
    global trumpImage
    # global obamaImage
    # global paulImage
    global spriteX
    global debug
    size(970,647)
    font = createFont("Arial", 100, True)
    textFont(font)
    backgroundImage = loadImage("stage2.png")
    hillaryImage = loadImage("hillary.png")
    trumpImage = loadImage("trump.png")
    Player1 = Player(1, 50, "neutral", False, 0, 0)
    Player2 = Player(2, 50, "neutral", False, 0, 0)
    # obamaImage = loadImage("obama.png")
    # paulImage = loadImage("paul.png")
    debug = "nothing"


def keyPressed():
    global Player1
    global Player2
    global debug
    ## Player1 Keys ##

    if(key == 'a' or key == 'A'):
        if (Player1.getLocked() == False):
            Player1.setMove(3)
            Player1.setLocked(True)

    if(key == 's' or key == 'S'):
        if (Player1.getLocked() == False):
            Player1.setMove(2)
            Player1.setLocked(True)

    if(key == 'd' or key == 'D'):
        if (Player1.getLocked() == False):
            Player1.setMove(1)
            Player1.setLocked(True)

    if(key == 'q' or key == 'Q'):
        if (Player1.getLocked() == False):
            Player1.setMove(6)
            Player1.setLocked(True)

    if(key == 'w' or key == 'W'):
        if (Player1.getLocked() == False):
            Player1.setMove(5)
            Player1.setLocked(True)

    if(key == 'e' or key == 'E'):
        if (Player1.getLocked() == False):
            Player1.setMove(4)
            Player1.setLocked(True)

    ## Player2 Keys ##

    if(key == 'j' or key == 'J'):
        if (Player2.getLocked() == False):
            Player2.setMove(3)
            Player2.setLocked(True)

    if(key == 'k' or key == 'K'):
        if (Player2.getLocked() == False):
            Player2.setMove(2)
            Player2.setLocked(True)

    if(key == 'l' or key == 'L'):
        if (Player2.getLocked() == False):
            Player2.setMove(1)
            Player2.setLocked(True)

    if(key == 'U' or key == 'u'):
        if (Player2.getLocked() == False):
            Player2.setMove(6)
            Player2.setLocked(True)

    if(key == 'i' or key == 'I'):
        if (Player2.getLocked() == False):
            Player2.setMove(5)
            Player2.setLocked(True)

    if(key == 'o' or key == 'O'):
        if (Player2.getLocked() == False):
            Player2.setMove(4)
            Player2.setLocked(True)



def draw():
    global Player1
    global Player2
    global debug
    global player1
    global player2
    background(backgroundImage)
    scale(0.55)
    image(hillaryImage, 500, 340)
    image(trumpImage, 1000, 320)
    if(Player1.getLocked()):
        player1 = "Ready"
    if(Player2.getLocked()):
        player2 = "Ready"
    text(Player1.getScore(), 400, 850)
    text(player1, 45, 835)
    text(Player2.getScore(), 1250, 850)
    text(player2, 1380, 835)
    # text(debug, 715, 100)
    # image(obamaImage, 150, 320)
    # image(paulImage, 1400, 320)
    if(Player1.getLocked() and Player2.getLocked()):
        roundResult(Player1, Player2)
        player1 = "Waiting"
        player2 = "Waiting"

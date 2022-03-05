import random
from gameClasses.classes import *
from gameLogic.display import *


class Game:

    def __init__(self, window, windowY, images):
        self.window = window
        self.windowY = windowY
        self.images = images
        self.colours = {'almond' : (245, 240, 225)}
        self.pillarX = 400
        self.offset = 0
        self.pillarGap = 135
        self.passed = False
        self.topPillar = Pillar(self.images, "top")
        self.bottomPillar = Pillar(self.images, "bottom")
        self.bird = Bird(self.windowY, self.images)
        self.scoreBoard = Display(self.images)
    
    def pillar_movement(self):
        if self.pillarX < -100:
            self.offset = random.randrange(-120, 120)
            self.passed = False
            self.pillarX = 400
        self.pillarX -= 5

    def current_pillar_rect(self, pillar):
        rect = pillar.get_pillar()
        rect[0] = self.pillarX
        if pillar.position == "top" : rect[1] = 0 - self.pillarGap - self.offset
        else : rect[1] = 360 + self.pillarGap - self.offset
        return rect
     
    def collision(self):
        topRect = self.current_pillar_rect(self.topPillar)
        bottomRect = self.current_pillar_rect(self.bottomPillar)
        if topRect.colliderect(self.bird.get_rect()) or bottomRect.colliderect(self.bird.get_rect()) : self.bird.dead = True
        elif not self.passed and topRect.right < self.bird.posX:
            self.scoreBoard.score += 1
            self.passed = True

    def reset(self):
        self.bird.dead = False
        self.scoreBoard.score = 0
        self.bird = Bird(self.windowY, self.images)
        self.topPillar = Pillar(self.images, "top")
        self.bottomPillar = Pillar(self.images, "bottom")
        self.pillarX = 400
        self.bird.gravity = 10
    
    def show_score(self):
        text = Text(200, 50, str(self.scoreBoard.score), self.colours['almond'], 50)
        text.display(self.window)
    
    def game_over(self):
        self.window.blit(self.scoreBoard.playImg, self.scoreBoard.playRect)
        self.window.blit(self.scoreBoard.scoreImg, self.scoreBoard.scoreRect)
        text = Text(200, 230, str(self.scoreBoard.score), self.colours['almond'], 50)
        text.display(self.window)

class Bird:

    def __init__(self, windowY, images):
        self.windowY = windowY
        self.images = images
        self.birdImages = [images['b1'], images['b2'], images['dead_b']]
        self.image = 0
        self.posX = 50
        self.posY = 350
        self.jump = 0
        self.jumpVelocity = 0
        self.gravity = 10
        self.dead = False
    
    def move(self):
        if self.dead:
            self.image = 2
            if self.posY < self.windowY - 30 : self.posY += self.gravity
        elif self.posY > 0:
            if self.jump:
                self.image = 1
                self.jumpVelocity -= 1
                self.posY -= self.jumpVelocity
            else:
                self.gravity += 0.2
                self.posY += self.gravity
        else:
            self.jump = 0
            self.posY += 3

    def dead_check(self):
        if self.posY >= self.windowY - 30 : self.dead = True
    
    def get_rect(self):
        imageRect = self.birdImages[self.image].get_rect()
        imageRect[0] = self.posX
        imageRect[1] = self.posY
        return imageRect


class Pillar:

    def __init__(self, images, position):
        self.images = images
        self.position = position
        
    def get_pillar(self):
        if self.position == "top" : return self.images['t_pillar'].get_rect()
        elif self.position == "bottom" : return self.images['b_pillar'].get_rect()

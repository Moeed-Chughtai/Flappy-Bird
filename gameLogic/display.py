import pygame


class Display:

    def __init__(self, images):
        self.scoreImg = images['score']
        self.playImg = images['play']
        self.scoreRect = images['score'].get_rect()
        self.playRect = images['play'].get_rect()
        self.align_menu()
        self.score = 0
    
    def align_menu(self):
        self.playRect.center = (200, 330)
        self.scoreRect.center = (200, 220)
    

class Text:
    
    def __init__(self, textX, textY, text, textColour, fontSize):
        self.textX = textX
        self.textY = textY
        self.text = text
        self.textColour = textColour
        self.fontSize = fontSize
    
    def display(self, window):
        font = pygame.font.Font('Font/nasalization-rg.otf', self.fontSize)
        textSurface = font.render(self.text, True, self.textColour)
        text = textSurface.get_rect()
        text.center = (self.textX, self.textY)
        window.blit(textSurface, text)

import pygame
from gameLogic.game import Game

pygame.init()
clock = pygame.time.Clock()

windowX, windowY = 400, 700
window = pygame.display.set_mode((windowX, windowY))
pygame.display.set_caption('Flappy Bird')

IMAGES = {}
images = ['background', 'b1', 'b2', 'dead_b', 'b_pillar', 't_pillar', 'play', 'score']
for image in images : IMAGES[image] = pygame.image.load('Images/' + image + '.png').convert_alpha()

game = Game(window, windowY, IMAGES)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.bird.jump = 17
                game.bird.gravity = 5
                game.bird.jumpVelocity = 10
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game.bird.dead and game.scoreBoard.playRect.collidepoint(event.pos):
                game.reset()

    window.blit(IMAGES['background'], (0, 0))
    window.blit(IMAGES['t_pillar'], (game.pillarX, 0 - game.pillarGap - game.offset))
    window.blit(IMAGES['b_pillar'], (game.pillarX, 360 + game.pillarGap - game.offset))
    window.blit(game.bird.birdImages[game.bird.image], (game.bird.posX, game.bird.posY))

    game.pillar_movement()
    game.bird.move()
    game.bird.dead_check()
    
    if not game.bird.dead:
        game.collision()
        game.show_score()
    else:
        game.game_over()
   
    clock.tick(60)
    pygame.display.flip()

import sys

import pygame

import mario
import config

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class Game():

    width = 640
    height = 480

    def __init__(self):
        self.pygame = pygame

    def init(self):
        self.pygame.init()
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)
        self.clock = self.pygame.time.Clock()
        # TODO: init sprite, tile,...
        self.mario_sprite = mario.Mario()

    def run(self):
        # main game loop
        while True:
            # hold frame rate at 60 fps
            self.clock.tick(1000)
            # enumerate event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                # sprite handle event
                self.handle(event)

            self.update()
            # re-draw screen
            self.draw(self.screen)

    def draw(self, screen):
        screen.fill(config.WHITE)
        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render("Hello World !", 1, (255, 0, 0))
            textpos = text.get_rect(centerx=self.width/2)
            self.screen.blit(text, textpos)
        # TODO: sprite draw
        self.mario_sprite.draw(self.screen)
        self.pygame.display.flip()

    def update(self):
        self.mario_sprite.update()

    def handle(self, event):
        self.mario_sprite.handle(event)

if __name__ == '__main__':
    g = Game()
    g.init()
    g.run()

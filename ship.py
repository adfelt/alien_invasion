import pygame

class Ship:
    '''A class to manage the ship'''
    def __init__(self):
        '''Initialize the ship and set it's starting position'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/space_ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.

    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)
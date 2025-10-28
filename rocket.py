import sys
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height)
        )
        pygame.display.set_caption('Moving Rocket')
        self.rocket = Rocket(self)

    def run(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.rocket.blitme()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up(event)
    
    def _check_key_down(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            self.rocket.horizontal_movement = event.key
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            self.rocket.vertical_movement = event.key
    
    def _check_key_up(self, event):
        if event.key == self.rocket.horizontal_movement:
            self.rocket.horizontal_movement = ''
        if event.key == self.rocket.vertical_movement:
            self.rocket.vertical_movement = ''

class Rocket:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('assets/player.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.vertical_movement = ''
        self.horizontal_movement = ''

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.horizontal_movement == pygame.K_RIGHT:
            self.rect.x += 1
        if self.horizontal_movement == pygame.K_LEFT:
            self.rect.x -= 1
        if self.vertical_movement == pygame.K_UP:
            self.rect.y -= 1
        if self.vertical_movement == pygame.K_DOWN:
            self.rect.y += 1

if __name__ == '__main__':
    game = Game()
    game.run()
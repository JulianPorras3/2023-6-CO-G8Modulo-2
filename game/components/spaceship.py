from pygame.sprite import  Sprite
import pygame
from game.components.bullets.bullet import Bulllet
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP

class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.bullets = pygame.sprite.Group()
        self.type = 'player'

    def update(self, user_input):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        
        if user_input[pygame.K_SPACE]:
            self.shoot()

        self.bullets.update()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.bullets.draw(screen)

    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        if self.rect.x + self.SHIP_WIDTH < 0:
            self.rect.x = SCREEN_WIDTH

    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        if self.rect.x > SCREEN_WIDTH:
            self.rect.x = -self.SHIP_WIDTH

    def move_up(self):
        if self.rect.y - self.SHIP_SPEED >= 0:
            self.rect.y -= self.SHIP_SPEED
    
    def move_down(self):
        if self.rect.y + self.SHIP_HEIGHT + self.SHIP_SPEED <= SCREEN_HEIGHT:
            self.rect.y += self.SHIP_SPEED

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.bullets.add(bullet)

class Bullet(Sprite):
    BULLET_WIDTH = 6
    BULLET_HEIGHT = 14
    BULLET_SPEED = 14

    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((self.BULLET_WIDTH, self.BULLET_HEIGHT))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self):
        self.rect.y -= self.BULLET_SPEED

        if self.rect.bottom <0:
            self.kill()

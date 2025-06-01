import pygame
from settings import *

class Player(pygame.sprite.Sprite):
  def __init__(self, groups, position):
    super().__init__(groups)
    self.image = pygame.image.load(join("resources", "images", "player", "down", "0.png")).convert_alpha()
    self.rect = self.image.get_frect(center=position)
    self.direction = pygame.Vector2()
    self.speed = 200

  def update(self, dt):
    keys = pygame.key.get_pressed()
    self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
    self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
    self.direction = self.direction.normalize() if self.direction else self.direction
    self.rect.center += self.speed * self.direction * dt

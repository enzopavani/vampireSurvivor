from settings import *
from math import atan2, degrees

class Sprite(pygame.sprite.Sprite):
  def __init__(self, groups, position, surface):
    super().__init__(groups)
    self.image = surface
    self.rect = self.image.get_frect(topleft=position)
    self.ground = True

class CollisionSprite(pygame.sprite.Sprite):
  def __init__(self, groups, position, surface):
    super().__init__(groups)
    self.image = surface
    self.rect = self.image.get_frect(topleft=position)

class InvisibleCollisionSprite(CollisionSprite):
  def __init__(self, groups, position, surface):
    super().__init__(groups, position, surface)
    self.image.set_alpha(0)

class Gun(pygame.sprite.Sprite):
  def __init__(self, groups, player):
    super().__init__(groups)
    self.gunSurface = pygame.image.load(join("resources", "images", "gun", "gun.png")).convert_alpha()
    self.player = player
    self.distance = 140
    self.playerDirection = pygame.Vector2(0, 1)
    self.image = self.gunSurface
    self.rect = self.image.get_frect(center = self.player.rect.center + self.playerDirection * self.distance)

  def getDirection(self):
    mousePosition = pygame.Vector2(pygame.mouse.get_pos())
    playerPosition = pygame.Vector2(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    self.playerDirection = (mousePosition - playerPosition).normalize()

  def rotateGun(self):
    angle = degrees(atan2(self.playerDirection.x, self.playerDirection.y)) - 90
    if self.playerDirection.x > 0:
      self.image = pygame.transform.rotozoom(self.gunSurface, angle, 1)
    else:
      self.image = pygame.transform.rotozoom(self.gunSurface, abs(angle), 1)
      self.image = pygame.transform.flip(self.image, False, True)

  def update(self, _):
    self.getDirection()
    self.rotateGun()
    self.rect.center = self.player.rect.center + self.playerDirection * self.distance

class Bullet(pygame.sprite.Sprite):
  def __init__(self, groups, surface, position, direction):
    super().__init__(groups)
    self.image = surface
    self.rect = self.image.get_frect(center = position)
    self.spawnTime = pygame.time.get_ticks()
    self.lifeTime = 2000

    self.direction = direction
    self.speed = 1000

  def update(self, dt):
    self.rect.center += self.direction * self.speed * dt

    if pygame.time.get_ticks() - self.spawnTime >= self.lifeTime:
      self.kill()
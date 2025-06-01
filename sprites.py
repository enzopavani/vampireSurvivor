from settings import *

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
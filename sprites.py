from settings import *

class CollisionSprite(pygame.sprite.Sprite):
  def __init__(self, groups, position, size):
    super().__init__(groups)
    self.image = pygame.Surface(size)
    self.image.fill("#0000ff")
    self.rect = self.image.get_frect(center=position)
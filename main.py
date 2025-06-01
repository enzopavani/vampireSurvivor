from settings import *
from player import Player
from sprites import *

from random import randint

class Game():
  def __init__(self):
    # setup
    self.displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Human Survivors")
    self.clock = pygame.time.Clock()
    self.running = True
    self.FPS = 60
    
    # groups
    self.allSprites = pygame.sprite.Group()
    self.collisionSprites = pygame.sprite.Group()
    
    # sprites
    self.player = Player(self.allSprites, (200, 300), self.collisionSprites)
    for i in range(6):
      x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
      w, h = randint(50, 100), randint(40, 100)
      CollisionSprite((self.allSprites, self.collisionSprites), (x, y), (w, h))

  def run(self):
    while self.running:
      dt = self.clock.tick(self.FPS) / 1000
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            self.running = False

      # update
      self.allSprites.update(dt)
      
      # draw
      self.displaySurface.fill("#000000")
      self.allSprites.draw(self.displaySurface)

      pygame.display.flip()
    pygame.quit()
      
if __name__ == "__main__":
  game = Game()
  game.run()
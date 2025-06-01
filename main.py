from settings import *
from player import Player

class Game():
  def __init__(self):
    self.displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Human Survivors")
    self.clock = pygame.time.Clock()
    self.running = True
    self.FPS = 60
    
    self.allSprites = pygame.sprite.Group()
    self.player = Player(self.allSprites, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

  def run(self):
    while self.running:
      dt = self.clock.tick(self.FPS) / 1000
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            self.running = False

      self.allSprites.update(dt)
      self.displaySurface.fill("#000000")
      self.allSprites.draw(self.displaySurface)

      pygame.display.flip()
    pygame.quit()
      
if __name__ == "__main__":
  game = Game()
  game.run()
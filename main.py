from settings import *

class Game():
  def __init__(self):
    self.displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Human Survivors")
    self.clock = pygame.time.Clock()
    self.running = True
    self.FPS = 60
    
    self.allSprites = pygame.sprite.Group()

  def run(self):
    while self.running:
      dt = self.clock.tick(self.FPS) / 1000
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            self.running = False

      self.displaySurface.fill("#000000")

      pygame.display.flip()
    pygame.quit()
      
if __name__ == "__main__":
  game = Game()
  game.run()
from settings import *
from player import Player
from sprites import *
from groups import *
from pytmx.util_pygame import load_pygame

from random import randint

class Game():
  def __init__(self):
    # setup
    self.displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Human Survivors")
    self.clock = pygame.time.Clock()
    self.running = True
    self.FPS = 60
    self.loadImages()
    
    # groups
    self.allSprites = AllSprites()
    self.collisionSprites = pygame.sprite.Group()
    self.bulletSprites = pygame.sprite.Group()

    self.setup()

    # gun timer
    self.canShoot = True
    self.shootTime = 0
    self.gunCooldown = 200
    
  def loadImages(self):
    self.bulletSurface = pygame.image.load(join("resources", "images", "gun", "bullet.png")).convert_alpha()

  def input(self):
    if pygame.mouse.get_pressed()[0] and self.canShoot:
      position = self.gun.rect.center + self.gun.playerDirection * 50
      Bullet((self.allSprites, self.bulletSprites), self.bulletSurface, position, self.gun.playerDirection)
      self.canShoot = False
      self.shootTime = pygame.time.get_ticks()
  
  def gunTimer(self):
    if not self.canShoot:
      currentTime = pygame.time.get_ticks()
      if currentTime - self.shootTime >= self.gunCooldown:
        self.canShoot = True

  def setup(self):
    map = load_pygame(join("resources", "data", "maps", "world.tmx"))
    for x, y, image in map.get_layer_by_name("Ground").tiles():
      Sprite(self.allSprites, (x * TILE_SIZE, y * TILE_SIZE), image)
    for obj in map.get_layer_by_name("Objects"):
      CollisionSprite((self.allSprites, self.collisionSprites), (obj.x, obj.y), obj.image)
    for obj in map.get_layer_by_name("Collisions"):
      InvisibleCollisionSprite(self.collisionSprites, (obj.x, obj.y), pygame.Surface((obj.width, obj.height)))
    for obj in map.get_layer_by_name("Entities"):
      if obj.name == "Player":
        self.player = Player(self.allSprites, (obj.x, obj.y), self.collisionSprites)
        self.gun = Gun(self.allSprites, self.player)

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
      self.gunTimer()
      self.input()
      self.allSprites.update(dt)
      
      # draw
      self.displaySurface.fill("#000000")
      self.allSprites.draw(self.player.rect.center)

      pygame.display.flip()
      print(self.bulletSprites)
    pygame.quit()
      
if __name__ == "__main__":
  game = Game()
  game.run()
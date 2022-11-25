import random

from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH, GAME_SPEED


class Clouds:
    def __init__(self):
        self.image = CLOUD
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.width = self.image.get_width()


    
    def update(self):
        self.x -= GAME_SPEED
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
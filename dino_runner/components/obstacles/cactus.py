import random

from dino_runner.components.obstacles.obstacle import Obstacle 
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

CACTUS = [(SMALL_CACTUS, 325), (LARGE_CACTUS, 300)]

class Cactus(Obstacle):
    def __init__(self, image):
        image, cactus_pos = CACTUS[random.randint(0, 1)]
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = cactus_pos

import pygame
import os

# Global Constants
TITLE = "Pink Cat Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
GAME_SPEED = 20 

# Assets Constants

START_TITLE = pygame.image.load(os.path.join(IMG_DIR, "Other/StartTitle.png"))

ICON = pygame.image.load(os.path.join(IMG_DIR, "CatWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CatRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CatRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CatRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CatRun2Shield.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CatDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CatRun2Hammer.png")),
]

RUNNING_INVISIBLE = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CatInvisible.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CatInvisible.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/CatJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/CatJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/CatJumpHammer.png"))
JUMPING_INVISIBLE = pygame.image.load(os.path.join(IMG_DIR, "Dino/CatInvisible.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CatDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CatDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CatDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CatDuck2Shield.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CatDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CatDuck2Hammer.png")),
]

DUCKING_INVISIBLE = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CatInvisible.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CatInvisible.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
INVISIBLE = pygame.image.load(os.path.join(IMG_DIR, 'Other/food.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

START = pygame.image.load(os.path.join(IMG_DIR, "Dino/CatStart.png"))

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))

RESTART = pygame.image.load(os.path.join(IMG_DIR, "Other/Reset.png"))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
INVISIBLE_TYPE = "invisible"

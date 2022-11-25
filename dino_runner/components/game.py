import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

FONT_STYLE = "freesansbold.ttf"


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.score = 0
        self.high_score = 0
        self.death_count = 0
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()
        
    def run(self): # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)
        
    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 2

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))

        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0

        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        self.draw_txt(f"SCORE: {self.score}", screen_width = 1000, screen_height = 50)
        self.draw_txt(f"HIGH SCORE: {self.high_score} ", screen_width = 840, screen_height = 50)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.draw_txt(f"{self.player.type.capitalize()}, enabled for {time_to_show} seconds", screen_width = 500, screen_height = 40)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN: #IT'S DIFFERENT OF K_DOWN.  K_DOWN = PgDn. KEYDOWN = Any pressioned key
                self.run()

    def draw_txt(self, message, screen_width, screen_height):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(message, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (screen_width, screen_height)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        self.screen.fill((225, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.draw_txt("Let's Gooo! Press any key to Start!", half_screen_width - 30, half_screen_height - 50)

        elif self.death_count > 0:
            self.game_speed = 20
            self.screen.blit(ICON, (half_screen_width - 60, half_screen_height - 200))
            self.draw_txt(f"Ooops! You Already Died: {self.death_count} Time(s)!", half_screen_width - 30, half_screen_height - 50)
            self.draw_txt(f"Your Final Score: {self.score}", half_screen_width - 50, half_screen_height - 10 )
            self.draw_txt("Do you wanna play again? Press any key to Restart!", half_screen_width - 40, half_screen_height + 50)

            


        pygame.display.update()
        self.handle_events_on_menu()
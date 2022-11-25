from dino_runner.utils.constants import INVISIBLE, INVISIBLE_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Invisible(PowerUp):
    def __init__(self):
        self.image = INVISIBLE
        self.type = INVISIBLE_TYPE
        super().__init__(self.image, self.type)
from pico2d import *
import play_state

class ground:
    def __init__(self):
        self.x =0
        self.y = 0
        self.image = load_image('MAP1.png')
        self.width = 1280
        self.hight = 1024

    def update(self):
        self.x -= play_state.player.dx
        self.y -= play_state.player.dy

        if (self.x < -1920):
            self.x += 3840
        if (self.x > 3200):
            self.x -= 3840
        if (self.y < -1424):
            self.y += 3072
        if (self.y > 2448):
            self.y -= 3072

    def draw(self):
            self.image.draw(self.x, self.y, self.width, self.hight)

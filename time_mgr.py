import enemies
import attack
import my_ch
import game_world
import framework
import game_completed
import play_state
from pico2d import*
class main_timer:
    def __init__(self):
        self.image = load_font('KO.TTF', 30)
        self.sec = 0
        self.min=0
    def update(self):
        self.sec +=0.05
        if self.sec >60:
            self.min+=1
            self.sec=0

        if self.min == 2:
            framework.change_state(game_completed)

        pass
    def draw(self):
        self.image.draw(640,950,f'{int(self.min)}분{int(self.sec)}초',(255,255,255))
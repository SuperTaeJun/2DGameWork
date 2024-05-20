from pico2d import*
import my_ch
import play_state
import framework
import gameover
class hp_bar:
    def __init__(self):
        self.image=load_image('hpbar.png')
        self.HP=100

    def draw(self):
        self.image.draw(640,470,self.HP/1.5,10)

    def update(self):
        self.HP=play_state.player.HP

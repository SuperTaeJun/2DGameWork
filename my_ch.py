from pico2d import*
import collide
import game_world
import framework
import gameover
import title
import play_state
class my_player:
    def __init__(self):
        self.character = load_image('characters_.png')
        self.player_x = 1280 // 2
        self.player_y = 1024 // 2
        self.dx=0
        self.dy=0
        self.dir =0
        self.frame = 0
        self.HP = 100

        #sound
        self.sound_check=True
        self.sound_main=load_music("main.ogg")

        #attack bool check
        self.at_1 = True
        self.at_2 = False
        self.at_3 = False
        self.at_4 = False

        self.GOD = False #무적모드

    def get_bb(self):
        return self.player_x-15,self.player_y-20,self.player_x+15,self.player_y+20
    def draw(self):

        if self.dx==0 and self.dy==0:
            if self.dir ==2: #오른쪽
                self.character.clip_draw(0, self.dir * 35, 27, 35, self.player_x, self.player_y, 60, 60)
            else: #왼쪽
                self.character.clip_draw(0, self.dir * 35, 27, 35, self.player_x, self.player_y, 60, 60)

        elif self.dx>0:
            self.character.clip_draw(self.frame * 28, self.dir * 35, 27, 35, self.player_x, self.player_y, 60, 60)

        elif self.dx<0:
            self.character.clip_draw(self.frame * 28, self.dir * 35, 27, 35, self.player_x, self.player_y, 60, 60)

        elif self.dy!=0:
            if self.dir ==3:
                self.character.clip_draw(self.frame * 28, self.dir * 35, 27, 35, self.player_x, self.player_y, 60, 60)
            else:
                self.character.clip_draw(self.frame * 28, self.dir * 35, 27, 35, self.player_x, self.player_y, 60, 60)
        ##draw_rectangle(*self.get_bb())
    def update(self):
        if self.GOD == True:
            self.HP =100
        self.frame = (self.frame + 1) % 7

        for i in range(len(game_world.objects[3])):
            if collide.collide_player(self,game_world.objects[3][i]):
                self.HP-=game_world.objects[3][i].power

        if self.HP <= 0:
            framework.change_state(title)
            self.at_2 = False
            self.at_3 = False
            self.at_4 = False


import random

from pico2d import *
import play_state
import collide
import game_world

def random_deg():
    global deg
    deg = random.randint(0,360)
    return deg
class font:
    image = None
    def __init__(self,monx,mony,damage):
        if font.image == None:
            font.image = load_font('damage.ttf', 20)
        self.x = monx-30
        self.y = mony-30
        self.damage = damage
        self.timer = 0
    def draw(self):
        self.image.draw(self.x,self.y,f'{self.damage}',(255,255,0))

    def update(self):
        self.x-=play_state.player.dx
        self.y-=play_state.player.dy
        if self.timer>1:
            game_world.remove_object(self)
        self.timer += 0.5



class basic_attack:
    attack=None
    def __init__(self):
        if basic_attack.attack==None:
            basic_attack.attack=load_image('basicat.png')
        self.ax=0
        self.power=10
        self.x=640
        self.y=512
        self.dir=0
        self.mon = random.randint(0,len(game_world.objects[3])-1)
        self.dx, self.dy = \
            ((game_world.objects[3][self.mon].x - self.x) / math.sqrt((game_world.objects[3][self.mon].x - self.x) ** 2 + (game_world.objects[3][self.mon].y - self.y) ** 2),
            (game_world.objects[3][self.mon].y - self.y) / math.sqrt((game_world.objects[3][self.mon].x - self.x) ** 2 + (game_world.objects[3][self.mon].y - self.y) ** 2))

        if play_state.player.dir == 3:
            self.speed = -25
        elif play_state.player.dir == 2:
            self.speed = 25
        else:
            self.speed = 25

    def get_bb(self):

        return self.x - 4, self.y - 4, self.x + 4, self.y + 4
    def draw(self):
        if game_world.objects[2][0].at_1:
            self.attack.clip_draw(0, 0, 30, 21, self.x, self.y)
        #draw_rectangle(*self.get_bb())

    def update(self):
        if game_world.objects[2][0].at_1:
            self.x -= play_state.player.dx
            self.y -= play_state.player.dy
            self.x += self.dx*self.speed
            self.y += self.dy*self.speed

            for i in range(len(game_world.objects[3])):
                if collide.collide_player(self,game_world.objects[3][i]):
                    game_world.add_object(font(game_world.objects[3][i].x, game_world.objects[3][i].y, self.power), 4)
                    game_world.remove_object(self)
                    game_world.objects[3][i].HP-=10

class circle_attack:
    def __init__(self):
        self.attack = load_image('circleat.png')
        self.power = 10
        self.x = 640
        self.y = 512
        self.timer = 0

    def get_bb(self):
        return self.x - 65, self.y - 65, self.x + 65, self.y + 65
    def draw(self):
        if game_world.objects[2][0].at_3:
            self.attack.clip_draw(0, 0, 112, 112, self.x, self.y,170,170)

    def update(self):
        if game_world.objects[2][0].at_3:
            for i in range(len(game_world.objects[3])):
                if collide.collide_player(self, game_world.objects[3][i]):
                    if self.timer > 1:
                        game_world.add_object(font(game_world.objects[3][i].x,game_world.objects[3][i].y,self.power),4)
                        game_world.objects[3][i].HP -= self.power
                        self.timer = 0

        self.timer += 0.2

class thunder:
    def __init__(self):
        self.image = load_image('thunder1.png')
        self.power = 8
        self.x = 640
        self.y = 512
        self.timer = 0
        self.timer_hit =0
        self.frame =0
        if play_state.player.dir == 2:
            self.dir = 1
        elif play_state.player.dir == 3:
            self.dir = -1
        else:
            self.dir = 1

    def get_bb(self):
        if self.dir == 1:
            return self.x + 20, self.y - 20, self.x + 200, self.y + 20
        elif self.dir == -1:
            return self.x - 200, self.y - 20, self.x - 20, self.y + 20

    def draw(self):
        if game_world.objects[2][0].at_2:
            if play_state.player.dir == 2:
                self.image.clip_draw(0, 19*self.frame, 98, 19, self.x+130*self.dir, self.y,200,50)
            elif play_state.player.dir == 3:
                self.image.clip_composite_draw(0, 19*self.frame, 98, 19, math.radians(180)," ",self.x+130*self.dir, self.y,200,50)
            else:
                self.image.clip_draw(0, 19 * self.frame, 98, 19, self.x + 130 * self.dir, self.y, 200, 50)
        #draw_rectangle(*self.get_bb())

    def update(self):
        if game_world.objects[2][0].at_2:
            if self.timer >0.6:
                game_world.remove_object(self)


            for i in range(len(game_world.objects[3])):
                if collide.collide_player(self, game_world.objects[3][i]):
                    game_world.add_object(font(game_world.objects[3][i].x, game_world.objects[3][i].y, self.power), 4)
                    game_world.objects[3][i].HP -= self.power

            self.frame+=1
            self.timer += 0.2
class rand_thunder:
    def __init__(self):
        self.deg = random_deg()
        self.image = load_image('random_thunder.png')
        self.power = 40
        self.x ,self.y = play_state.player.player_x+(math.cos(math.radians(self.deg))*300),\
                         play_state.player.player_y+(math.sin(math.radians(self.deg))*300)
        self.timer = 0
        self.frame = 0

    def get_bb(self):
            return self.x - 80, self.y - 220, self.x + 80, self.y - 100

    def draw(self):
        if game_world.objects[2][0].at_4:
            self.image.clip_draw(700* self.frame, 0, 700, 700, self.x, self.y, 400, 400)

    def update(self):
        if game_world.objects[2][0].at_4:
            self.x -= play_state.player.dx
            self.y -= play_state.player.dy
            if self.timer > 0.6:
                game_world.remove_object(self)

            for i in range(len(game_world.objects[3])):
                if collide.collide_player(self, game_world.objects[3][i]):
                    game_world.add_object(font(game_world.objects[3][i].x, game_world.objects[3][i].y, self.power), 4)
                    game_world.objects[3][i].HP -= self.power

            self.frame = (self.frame + 1) % 4
            self.timer += 0.15
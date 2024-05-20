from pico2d import *
import random
import os
import math
import collide
import game_world
import play_state
import Map
import my_ch


deg=None
def random_deg():
    global deg
    deg = random.randint(0,360)
    return deg
class skeleton_many :
    image = None
    die_image = None
    def __init__(self):
        self.frame = 0
        self.direction =0
        self.x, self.y = random.randint(play_state.player.player_x-300,play_state.player.player_x+300) ,\
                         random.randint(-200,0)
        self.dx = 0
        self.dy = 0
        self.speed = 20
        self.HP = 15
        self.power = 2
        self.time_die =0
        self.die_state=False
        if skeleton_many.image == None:
            skeleton_many.image = load_image('skelton.png')
        if skeleton_many.die_image == None:
            skeleton_many.die_image = load_image('die.png')
        self.die_sound=load_wav("die.wav")
    def get_bb(self):
        return self.x-15, self.y-15, self.x+15, self.y+15

    def draw(self):
        if self.die_state == False:
            self.image.clip_draw(self.frame * 30, self.direction * 56, 30, 56, self.x, self.y, 50, 60)
        elif self.die_state == True:
            self.die_image.clip_draw(0, 0, 81, 81, self.x, self.y, 50, 60)

    def update(self):
        self.y += self.speed
        self.x -= play_state.player.dx
        self.y -= play_state.player.dy
        if 640 > self.x:
            self.direction = 0
        elif 640 < self.x:
            self.direction = 1
        self.frame = (self.frame + 1) % 6

        if self.y > 1300:
            game_world.remove_object(self)

        if self.HP < 0:
            if self.HP < 0:
                self.die_state = True
                self.time_die += 1
                if self.time_die > 5:
                    self.die_sound.play(1)
                    game_world.remove_object(self)


class skeleton :
    image = None
    die_image = None
    def __init__(self):
        self.deg = random_deg()
        self.frame = 0
        self.direction =0
        self.x, self.y = play_state.player.player_x+(math.cos(math.radians(self.deg))*700),\
                         play_state.player.player_y+(math.sin(math.radians(self.deg))*650)
        self.dx = 0
        self.dy = 0
        if game_world.objects[4][0].sec >= 30 and game_world.objects[4][0].min ==0 :
            self.HP = 20
            print(self.HP)
        elif game_world.objects[4][0].min == 1 and game_world.objects[4][0].sec < 30:
            self.HP = 25
            print(self.HP)
        elif game_world.objects[4][0].min == 1 and game_world.objects[4][0].sec > 30:
            self.HP = 35
        elif game_world.objects[4][0].sec <= 30 and game_world.objects[4][0].min == 0 :
            self.HP = 15
        self.power = 2
        self.speed = 5
        self.time_die =0
        self.die_state=False
        if skeleton.image == None :
            skeleton.image = load_image('skelton.png')
        if skeleton.die_image == None :
            skeleton.die_image = load_image('die.png')
        self.die_sound =load_wav("die.wav")
        self.die_sound.set_volume(80)

        #시간이 지남에 따라 강해짐
        self.upgrade=0
    def get_bb(self):
        return self.x-15, self.y-15, self.x+15, self.y+15

    def draw(self):
        if self.die_state ==False:
            self.image.clip_draw(self.frame*30,self.direction*56, 30, 56, self.x, self.y, 50, 60)
        elif self.die_state==True:
            self.die_image.clip_draw(0, 0, 81, 81, self.x, self.y, 50, 60)
        #draw_rectangle(*self.get_bb())

    def update(self):#, player_x, player_y):


        print(self.HP)
        self.dx, self.dy = (( play_state.player.player_x - self.x) / math.sqrt((play_state.player.player_x - self.x) ** 2 + (play_state.player.player_y - self.y) ** 2),
                            (play_state.player.player_y - self.y) / math.sqrt((play_state.player.player_x - self.x) ** 2 + (play_state.player.player_y - self.y) ** 2))

        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        self.x -= play_state.player.dx
        self.y -= play_state.player.dy

        if 640 > self.x:
            self.direction = 0
        elif 640 < self.x:
            self.direction = 1
        self.frame = (self.frame + 1) % 6

        if self.HP<0:
            self.die_state=True
            self.time_die+=1
            if self.time_die>5:
                self.die_sound.play(1)
                game_world.remove_object(self)

class zombie:
    image = None
    die_image = None
    def __init__(self):
        self.deg = random_deg()
        self.frame = 0
        self.direction = 0
        self.x, self.y = play_state.player.player_x+(math.cos(math.radians(self.deg))*700),\
                         play_state.player.player_y+(math.sin(math.radians(self.deg))*650)
        self.dx = 0
        self.dy =0
        if game_world.objects[4][0].sec >= 30 and game_world.objects[4][0].min ==0 :
            self.HP = 40
            self.speed = 4
            print(self.HP)
        elif game_world.objects[4][0].min == 1 and game_world.objects[4][0].sec < 30:
            self.HP = 40
            self.speed = 5
            print(self.HP)
        elif game_world.objects[4][0].min == 1 and game_world.objects[4][0].sec > 30:
            self.HP = 40
            self.speed = 6
        elif game_world.objects[4][0].sec <= 30 and game_world.objects[4][0].min == 0 :
            self.HP = 30
            self.speed = 4
        self.power = 4
        self.time_die =0
        self.die_state=False
        if zombie.image == None:
            zombie.image = load_image('zombie1.png')
        if zombie.die_image == None :
            zombie.die_image = load_image('die.png')
        self.die_sound = load_wav("die.wav")
    def draw(self):
        if self.die_state == False:
            self.image.clip_draw(self.frame*31,self.direction*73,31,73,self.x,self.y,60,80)
        elif self.die_state == True:
            self.die_image.clip_draw(0, 0, 81, 81, self.x, self.y, 50, 60)
        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return (self.x-15,self.y-20,self.x+15,self.y+20)
    def update(self):#, player_x, player_y):
        self.dx, self.dy = ((play_state.player.player_x-self.x)/math.sqrt((play_state.player.player_x-self.x)** 2+(play_state.player.player_y-self.y) ** 2),
                          (play_state.player.player_y-self.y)/math.sqrt((play_state.player.player_x-self.x)** 2+(play_state.player.player_y-self.y) ** 2))

        self.x += self.dx*self.speed
        self.y += self.dy*self.speed
        self.x -= play_state.player.dx
        self.y -= play_state.player.dy
        if 640 > self.x:
            self.direction = 0
        elif 640 < self.x:
            self.direction = 1
        self.frame = (self.frame + 1) % 6

        if self.HP<0:
            if self.HP < 0:
                self.die_state = True
                self.time_die += 1
                if self.time_die > 5:
                    self.die_sound.play(1)
                    game_world.remove_object(self)

class bat :
    image = None
    die_image = None
    def __init__(self):
        self.deg = random_deg()
        self.frame = 0
        self.direction =0
        self.x, self.y = play_state.player.player_x+(math.cos(math.radians(self.deg))*700),\
                         play_state.player.player_y+(math.sin(math.radians(self.deg))*650)
        self.dx = 0
        self.dy = 0
        if game_world.objects[4][0].sec >= 30 and game_world.objects[4][0].min == 0 :
            self.HP = 120
            self.speed = 5
            print(self.HP)
        elif game_world.objects[4][0].min == 1 and game_world.objects[4][0].sec < 30:
            self.HP = 120
            self.speed = 7
            print(self.HP)
        elif game_world.objects[4][0].min == 1 and game_world.objects[4][0].sec > 30:
            self.HP = 150
            self.speed = 7
        elif game_world.objects[4][0].sec <= 30 and game_world.objects[4][0].min == 0 :
            self.HP = 100
            self.speed = 5
        self.power = 10
        self.time_die =0
        self.die_state=False
        if bat.image == None :
            bat.image = load_image('bat.png')
        if bat.die_image == None :
            bat.die_image = load_image('die.png')
        self.die_sound = load_wav("die.wav")
    def get_bb(self):
        return self.x-20, self.y-30, self.x+20, self.y+30

    def draw(self):
        if self.die_state ==False:
            self.image.clip_draw(self.frame*134,self.direction*170, 134, 170, self.x, self.y, 90, 120)
        elif self.die_state==True:
            self.die_image.clip_draw(0, 0, 81, 81, self.x, self.y, 50, 60)
        #draw_rectangle(*self.get_bb())

    def update(self):
        self.dx, self.dy = (( play_state.player.player_x - self.x) / math.sqrt((play_state.player.player_x - self.x) ** 2 + (play_state.player.player_y - self.y) ** 2),
                            (play_state.player.player_y - self.y) / math.sqrt((play_state.player.player_x - self.x) ** 2 + (play_state.player.player_y - self.y) ** 2))

        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
        self.x -= play_state.player.dx
        self.y -= play_state.player.dy
        if 640 > self.x:
            self.direction = 1
        elif 640 < self.x:
            self.direction = 0
        self.frame = (self.frame + 1) % 6

        if self.HP <= 0:
            self.die_state=True
            self.time_die+=1
            if self.time_die>5:
                self.die_sound.play(1)
                game_world.remove_object(self)

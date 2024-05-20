from pico2d import *
import Map
import my_ch
import enemies
import framework
import gameover
import game_world
import collide
import attack
import time_mgr
import ui
import store
def handle_events(): # dir=3 왼쪽 dir =4 오른쪽

    global player
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                framework.push_state(store)
            elif event.key == SDLK_LEFT:
                player.dx = -10
                player.dir = 3
            elif event.key == SDLK_RIGHT:
                player.dx = 10
                player.dir = 2
            elif event.key == SDLK_UP:
                player.dy = 10
            elif event.key == SDLK_DOWN:
                player.dy = -10
            elif event.key == SDLK_g:
                game_world.objects[2][0].GOD = True
            elif event.key == SDLK_h:
                game_world.objects[2][0].GOD = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                player.dy = 0
            elif event.key == SDLK_DOWN:
                player.dy = 0

            elif event.key == SDLK_LEFT:
                player.dx = 0
                player.dir=3
            elif event.key == SDLK_RIGHT:
                player.dx = 0
                player.dir=2

player = None
MAP = None
skeleton = None
zombie = None
skeleton_many = None
sound_check = None
sound_main= None
#at = None
open_canvas()
def enter():
    maplist = [[-1280, 1024], [0, 1024], [1280, 1024], [-1280, 0], [0, 0], [1280, 0], [-1280, -1024], [0, -1024],
             [1280, -1024]]
    global player
    global MAP
    global z_list_size
    global MAPS
    global skeleton_many
    global font_time
    global main_time
    global sound_check
    global sound_main
    if player == None:
        player = my_ch.my_player()

    MAPS = [Map.ground() for i in range(0,9)]
    for i in range(9):
        MAPS[i].x = maplist[i][0]
        MAPS[i].y = maplist[i][1]
    for i in range(9):
        game_world.add_object(MAPS[i],0)
    main_time=0
    game_world.add_object(time_mgr.main_timer(), 4)
    game_world.add_object(ui.hp_bar(),4)
    game_world.add_object(player,2)

    game_world.add_object(attack.circle_attack(),1)
    game_world.add_object(enemies.zombie(), 3)
    game_world.add_object(enemies.skeleton(), 3)

    # sound
    sound_check = True
    sound_main = load_music("main.ogg")

def exit():
    game_world.objects[2][0].HP = 100
    game_world.objects[2][0].sound_main.stop()
    game_world.clear()


time_mon_s = 0
time_mon_z = 0
time_mon_b = 0
time_a_b = 0
time_m_s =0
time_a_t =0
time_a_rt =0
def update():
    global time_mon_s
    global time_mon_z
    global time_mon_b
    global time_a_b
    global time_m_s
    global skeleton_many
    global zombies
    global skeleton
    global time_a_t
    global time_a_rt
    #몬스터 타이머
    time_mon_b += 0.01
    time_mon_s += 0.04
    time_mon_z += 0.04
    time_m_s += 0.01
    #공격 타이머
    if game_world.objects[2][0].at_1:
        time_a_b += 0.2
    if game_world.objects[2][0].at_2:
        time_a_t += 0.05
    if game_world.objects[2][0].at_4:
        time_a_rt += 0.03
    basic_at = [attack.basic_attack() for i in range(2)]

    #======================================================================

    if time_a_rt >=1:
        game_world.add_object(attack.rand_thunder(), 1)
        time_a_rt=0


    if time_a_t >=1:
        game_world.add_object(attack.thunder(), 1)
        time_a_t=0

    if time_m_s >= 2:
        skeleton_many = [enemies.skeleton_many() for i in range(50)]
        time_m_s=0
        game_world.add_objects(skeleton_many, 3)

    if time_a_b>=1:
        time_a_b=0
        game_world.add_objects(basic_at, 1)

    if time_mon_s >= 1:
        time_mon_s = 0
        game_world.add_object(enemies.skeleton(), 3)
    if time_mon_z >= 1:
        game_world.add_object(enemies.zombie(), 3)
        time_mon_z = 0
    if time_mon_b >= 1:
        game_world.add_object(enemies.bat(), 3)
        time_mon_b = 0

    for game_Object in game_world.all_objects():
        game_Object.update()

def draw_world():
    for game_Object in game_world.all_objects():
        game_Object.draw()
def draw():
    clear_canvas()
    for game_Object in game_world.all_objects():
        game_Object.draw()

    global sound_check
    global sound_main
    if sound_check:
        sound_main.play(3)
        sound_check = False
    update_canvas()
def pause():
    pass

def resume():
    pass

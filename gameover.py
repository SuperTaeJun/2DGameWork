from pico2d import *

import framework
import title
import play_state
image = None

def enter():
    global image
    image = load_image('gameOver.png')
    # fill here
    pass

def exit():
    global image
    del image
    # fill here
    pass

def handle_events():
    # fill here
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE :
            framework.change_state(title)

def draw():
    clear_canvas()
    image.draw(640,515,1280,1024)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass



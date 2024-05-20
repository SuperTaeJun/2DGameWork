import attack
from pico2d import*
import framework
import play_state
import game_world
import title
def enter():
    global image
    image = load_image('store.png')
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
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_1:
                game_world.objects[2][0].at_1 = True
                print(game_world.objects[2][0].at_1)
                pass
            elif event.key == SDLK_2:
                play_state.player.at_2 = True
                pass
            elif event.key == SDLK_3:
                play_state.player.at_3 = True
                pass
            elif event.key == SDLK_4:
                play_state.player.at_4 = True
                pass
            elif event.key == SDLK_r:
                framework.change_state(title)
            elif event.key == SDLK_ESCAPE:
                framework.pop_state()


def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(640,500,1280,1024)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass


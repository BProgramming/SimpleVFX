import pygame
import SimpleVFX as sVFX
from os.path import join

pygame.init()
WIDTH, HEIGHT = 500, 300
FPS_TARGET = 60
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.SCALED)

class example_obj:
    def __init__(self):
        self.rect = pygame.Rect(100, 100, 100, 100)

def main(win):
    clock = pygame.time.Clock()

    manager = sVFX.VisualEffectsManager(join("example"), generate_mirrors=False, default_time=5000.0)
    src = example_obj()

    alive_time = 0
    while True:
        win.fill(color="white")
        dtime = clock.tick(FPS_TARGET)
        alive_time += dtime

        if len(manager.active_effects.items()) == 0 and alive_time < manager.default_time:
            manager.spawn(sVFX.VisualEffect(src, manager.image_master, "EXAMPLE", scale=(200.0, 200.0)))
        else:
            manager.loop(dtime, win)

        if alive_time > 2 * manager.default_time:
            alive_time = 0
        pygame.display.update()

if __name__ == "__main__":
    main(WINDOW)

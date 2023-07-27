import map, pygame, configparser

#SCREEN
MAP_WINDOW_HEIGHT: int
MAP_WINDOW_WIDTH: int
SCREEN: pygame.surface

def _load_setting():
    global MAP_WINDOW_HEIGHT, MAP_WINDOW_WIDTH, SCREEN
    setting = configparser.ConfigParser()
    setting.read("./setting.config")
    MAP_WINDOW_HEIGHT = int(setting['MAP-DEFAULT']['DisplayWindowHeight'])
    MAP_WINDOW_WIDTH = int(setting['MAP-DEFAULT']['DisplayWindowWidth'])
    SCREEN = pygame.display.set_mode((MAP_WINDOW_WIDTH, MAP_WINDOW_HEIGHT))


def main():
    loop = True
    pygame.init()
    _load_setting()
    while loop:
        map.load(1, MAP_WINDOW_HEIGHT, MAP_WINDOW_WIDTH, SCREEN)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                loop = False
    pygame.quit()

if __name__ == '__main__':
    main()
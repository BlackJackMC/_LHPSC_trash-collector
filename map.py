import pygame

# SCREEN SIZE
MAP_WINDOW_HEIGHT: int
MAP_WINDOW_WIDTH: int
SCREEN: pygame.Surface

# GRID SIZE
GRID_WIDTH: int
GRID_HEIGHT: int


def _read_map(map_id: int):
    game_map = []
    with open(f"./data/{map_id}.txt") as f:
        for line in f.readlines():
            temp = []
            for item in line.split(" "):
                if item:
                    temp.append(int(item))
            game_map.append(temp)
    return game_map

def draw_cell(
    curr_x: int,
    curr_y: int,
    image: pygame.Surface = None,
    color: tuple = None,
    margin: int = 1
):
    if image is not None:
        image_x = curr_y * GRID_WIDTH + round((GRID_WIDTH - image.get_size()[1]) / 2)
        image_y = curr_x * GRID_HEIGHT + round((GRID_HEIGHT - image.get_size()[0]) / 2)
        SCREEN.blit(image, (image_x, image_y))
    elif color is not None:
        pygame.draw.rect(
            SCREEN,
            color,
            pygame.Rect(
                curr_y * GRID_WIDTH + margin,
                curr_x * GRID_HEIGHT + margin,
                GRID_WIDTH - 2 * margin,
                GRID_HEIGHT - 2 * margin,
            ),
        )
    else:
        raise Exception("Invalid argument")

def _image_scale(image: pygame.Surface, margin: int = 1):
    return pygame.transform.scale(
        image, (int(GRID_WIDTH - 2 * margin), int(GRID_HEIGHT - 2 * margin))
    )

def _render_map(game_map: list[list[int]]):
    global GRID_WIDTH, GRID_HEIGHT, OBSTACLE, TRASH
    margin = 1
    map_width = len(game_map)
    map_height = len(game_map[0])
    GRID_WIDTH = MAP_WINDOW_WIDTH / map_width
    GRID_HEIGHT = MAP_WINDOW_HEIGHT / map_height

    WATER: tuple = (3, 190, 252)
    MOUNTAIN: tuple = (100, 100, 100)
    BACKGROUND: tuple = (0, 0, 0)
    OBSTACLE = pygame.image.load("./icon/iceberg.png").convert_alpha()
    TRASH = pygame.image.load("./icon/trash.png").convert_alpha()

    SCREEN.fill(BACKGROUND)

    OBSTACLE = _image_scale(OBSTACLE, margin)
    TRASH = _image_scale(TRASH, margin)


    for i in range(map_height):
        for j in range(map_width):
            draw_cell(i, j, color = WATER)
            if game_map[i][j] == 3:
                draw_cell(i, j, color = MOUNTAIN)
            elif game_map[i][j] == 0:
                draw_cell(i, j, image = TRASH)
            elif game_map[i][j] == 1:
                draw_cell(i, j, image = OBSTACLE)

def load(map_id: int, map_window_height: int, map_window_width: int, screen: pygame.Surface):
    global MAP_WINDOW_HEIGHT, MAP_WINDOW_WIDTH, SCREEN
    MAP_WINDOW_HEIGHT = map_window_height
    MAP_WINDOW_WIDTH = map_window_width
    SCREEN = screen
    _render_map(_read_map(map_id))
    pygame.display.update()

def main():
    print("A module to load game maps from data folder")
    print("Please import from another file to use")


if __name__ == "__main__":
    main()

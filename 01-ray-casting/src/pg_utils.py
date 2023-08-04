import pyglet as pg

from typing import List, Tuple

from environment import PlayerState

def show_birdseye(player_state: PlayerState, map_grid: List[str], window_size: Tuple[int, int]):
    # Size the map to fit in the window
    cell_size = min(window_size[0] / len(game_map[0]), window_size[1] / len(game_map))

    batch = pg.graphics.Batch()
    space: List = []
    for row, block in enumerate(map_grid):
        for col, cell in enumerate(block):
            # Draw open space as a white block
            bottom_left_x = col * cell_size
            bottom_left_y = row * cell_size
            color = (250, 248, 184) if cell != "#" else (11, 42, 109)
            space.append(pg.shapes.Rectangle(x=bottom_left_x, y=bottom_left_y,
                                             width=cell_size, height=cell_size, color=color,
                                             batch=batch))

    player_icon = pg.shapes.Circle(player_state.x * cell_size, player_state.y * cell_size,
                                   int(cell_size/4), color=(255, 30, 30),
                                   batch=batch)

    batch.draw()


if __name__ == '__main__':
    screen: Tuple[int, int] = (700, 700)
    birdseye_window = pg.window.Window(screen[0], screen[1], "Bird's Eye View", vsync=False)

    # Set up our initial player state and game map
    player: PlayerState = PlayerState(x=2.5,
                                      y=2.5,
                                      angle=0.0,
                                      step_size=0.045)

    game_map: List[str] = ['################',
                           '#            # #',
                           '#         ## # #',
                           '#       #  #   #',
                           '# #   # #### ###',
                           '#        ##    #',
                           '#   #       ## #',
                           '##            ##',
                           '###           ##',
                           '#            # #',
                           '#         ## # #',
                           '#       #  #   #',
                           '# #   # #### ###',
                           '# ### #  ##    #',
                           '#   #       ## #',
                           '################'
                           ]

    @birdseye_window.event
    def on_draw():
        birdseye_window.clear()
        show_birdseye(player, game_map, screen)


    pg.app.run()

import pyglet as pg
from typing import List, Tuple

from environment import GameEnvironment, PlayerState


# Set up our initial player state and game map


player: PlayerState = PlayerState(x = 2.5,
                                  y = 2.5,
                                  angle = 0.0,
                                  step_size = 0.045)

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
                       '################']


if __name__ == '__main__':
    game = GameEnvironment(player=player, game_map=game_map)

    # Start the game window with the initial player view
    window = pg.window.Window(screen[0], screen[1], "Ray Casting", vsync=False)
    debug_window = pg.window.Window(screen[0], screen[1], "Bird's Eye View", vsync=False)

    @window.event
    def on_draw():
        window.clear()
        game.render_view()


    @debug_window.event
    def on_draw():
        debug_window.clear()
        game.render_debug_view()

    @window.event
    def on_key_press(symbol):
        if symbol == pg.window.key.ESCAPE:
            window.close()

        if symbol == pg.window.key.UP:
            game.update_player(up=True)
        elif symbol == pg.window.key.DOWN:
            game.update_player(down=True)
        elif symbol == pg.window.key.LEFT:
            game.update_player(left=True)
        elif symbol == pg.window.key.RIGHT:
            game.update_player(right=True)

        # Recompute the walls to render on player movement
        game.walls = get_view()

    pg.app.run()
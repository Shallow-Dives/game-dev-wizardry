import pyglet as pg

from dataclasses import dataclass
from math import pi, floor, sin, cos
from typing import List, Tuple

@dataclass
class PlayerState:
    x: float
    y: float
    angle: float
    step_size: float

@dataclass
class PlayerView:
    # Set up the player's view within the map
    fov: float = pi / 2.7  # Player field of view
    half_fov = fov * 0.5
    angle_step: float = fov / 160  # The angle between rays
    wall_height: float = 100.0  # Wall height in pixels at one distance unit
    screen: Tuple[int, int] = (700, 700)


class GameEnvironment:

    def __init__(self, player: PlayerState, game_map: List[str]):
        self.player = player
        self.game_map = game_map


    def update_player(self, up: bool=False, down: bool=False,
                            left: bool=False, right: bool=False):
        """Update the player state based on the keyboard input"""
        prev_position = (self.player.x, self.player.y)

        # Calculate our step along player angle
        x_step = cos(self.player.angle) * self.player.step_size
        y_step = -sin(self.player.angle) * self.player.step_size

        if up:
            self.player.x += x_step
            self.player.y += y_step
        if down:
            self.player.x -= x_step
            self.player.y -= y_step
        if right:
            self.player.angle -= self.player.step_size
        if left:
            self.player.angle += self.player.step_size

        # Only step if we aren't going to end up inside a wall
        if self.point_is_wall(self.player.x, self.player.y):
            (self.player.x, self.player.y) = prev_position

    def point_is_wall(self, x: float, y: float) -> bool:
        """Determine if a given point in the map is in a wall"""
        return True if self.game_map[floor(x)][floor(y)] == '#' else False


    def render_debug_view(self):
        pass


    def render_view(self, walls: List[float]):
        batch = pg.graphics.Batch()

        batch.draw()

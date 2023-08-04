from math import pi, dist, floor, ceil, tan
from typing import List

from environment import PlayerView


def cast_horizontal_ray(self, view_angle: float):
    # Determine if the player angle is "facing up" within the map
    facing_up: bool = abs(floor(view_angle / pi) % 2.0) != 0.0

    # Find the ray extension values
    dy = 1.0 if facing_up else -1.0
    dx = -dy / tan(view_angle)

    # Determine the first grid lines the ray intersects with
    # This is where our ray starts
    if facing_up:
        ray_y = ceil(self.player.y) - self.player.y
    else:
        ray_y = floor(self.player.y) - self.player.y
    ray_x = -ray_y / tan(view_angle)

    # Step the ray along the grid intersections until we hit a wall
    while True:
        # Move the ray forward one step relative to the player
        ray_x += dx
        ray_y += dy

        # Determine the ray's current absolute map coordinates
        ray_x_world = ray_x + self.player.x
        ray_y_world = ray_y + self.player.y
        if not facing_up:
            ray_y_world -= 1.0

        # Check if our ray has hit a wall
        print("Horizontal x, y", ray_x_world, ray_y_world)
        print("Map location", floor(ray_x_world), floor(ray_y_world))
        if self.point_is_wall(ray_x_world, ray_y_world):
            break

    return dist((self.player.x, self.player.y), (ray_x, ray_y))


def cast_vertical_ray(self, view_angle: float):
    # Determine if the player angle is "facing right" within the map
    facing_right: bool = abs(floor((view_angle - pi / 2.0) / pi) % 2.0) != 0.0

    # Find the ray extension values
    dx = 1.0 if facing_right else -1.0
    dy = dx * -tan(view_angle)

    # Determine the first grid lines the ray intersects with
    # This is where our ray starts
    if facing_right:
        ray_x = ceil(self.player.x) - self.player.x
    else:
        ray_x = floor(self.player.x) - self.player.x
    ray_y = -ray_x * tan(view_angle)

    # Step the ray along the grid intersections until we hit a wall
    while True:
        # Move the ray forward one step relative to the player
        ray_x += dx
        ray_y += dy

        # Determine the ray's current absolute map coordinates
        ray_y_world = ray_y + self.player.y
        ray_x_world = ray_x + self.player.x
        if not facing_right:
            ray_x_world -= 1.0

        # Check if our ray has hit a wall
        if self.point_is_wall(ray_x_world, ray_y_world):
            break

    return dist((self.player.x, self.player.y), (ray_x, ray_y))


def get_view(player_angle: float, view: PlayerView) -> List[float]:
    """
    Returns:
        List[float]: A list of the wall heights to render across the player's view
    """
    # Determine where the player is "looking"
    start_angle: float = player_angle + view.half_fov

    walls: List[float] = [0] * 160
    for wall_index in range(len(walls)):
        # Determine the wall's angle w.r.t. the player's view
        view_angle: float = start_angle - float(wall_index) * view.angle_step

        # Get the distance to the closest wall intersection
        horizontal_delta = cast_horizontal_ray(view_angle)
        vertical_delta = cast_vertical_ray(view_angle)
        closest_wall_delta: float = min(horizontal_delta, vertical_delta)
        print(wall_index, closest_wall_delta)

        # Convert the closest ray intersection distance to wall height
        walls[wall_index] = view.wall_height / closest_wall_delta
        print("Wall: ", wall_index, walls[wall_index])

    return walls

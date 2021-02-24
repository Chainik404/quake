import pygame
from settings import *
from map import world_map
import math

def ray_casting(sc, player_pos, player_angle):
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_pos
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            #pygame.draw.line(sc, DARKGRAY, player_pos, (x, y),2)
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                depth *= math.cos(player_angle - cur_angle)
                proj_heght = PROJ_COEFF / depth
                c = 225 / (1 + depth * depth * 0.0001)
                color = (c // 2, c, c // 2)
                pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_heght // 2, SCALE, proj_heght))
                break
        cur_angle += DELTA_ANGLE

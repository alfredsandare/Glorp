import pygame

from util import rectangles_overlap


class Chunk:
    def __init__(self, x_pos: int, y_pos: int, tiles: list[str]):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.tiles = tiles

    def render(self, screen: pygame.Surface, images, 
               camera_x: int, camera_y: int, camera_zoom: int):

        TILE_SIZE = 16 * camera_zoom
        screen_size = screen.get_size()
        for i, tile in enumerate(self.tiles):
            # in-game coordinates, measured in tiles
            x = i%16 + 16*self.x_pos - camera_x
            y = i//16 + 16*self.y_pos - camera_y

            # convert to pixel coordinates
            x = TILE_SIZE*x + screen_size[0]//2
            y = TILE_SIZE*y + screen_size[1]//2

            if not rectangles_overlap(x, y, x+TILE_SIZE, 
                                      y+TILE_SIZE, 0, 0, *screen_size):
                continue

            image = pygame.transform.scale_by(images[tile], camera_zoom)
            screen.blit(image, (x, y))

import pygame


class Chunk:
    def __init__(self, x_pos: int, y_pos: int, tiles: list[str]):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.tiles = tiles

    def render(self, screen: pygame.Surface, images):
        for i, tile in enumerate(self.tiles):
            x, y = i%16, i//16
            screen.blit(images[tile], (x, y))

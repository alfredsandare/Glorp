import json
import os
import platform
import pygame

from chunk import Chunk
from util import is_valid_image


pygame.init()
DIR_SEPARATOR = "/"
if platform.system == "Windows":
    DIR_SEPARATOR = "\\"
PATH = DIR_SEPARATOR.join(__file__.split(DIR_SEPARATOR)[:-1]) + DIR_SEPARATOR


class Game:
    def __init__(self):
        # self.player = Player()
        self.chunks = self._load_world_data()
        self.running = True
        self.resolution = (1280, 720)
        self.screen = pygame.display.set_mode(self.resolution)
        self.camera_x = 0  # unit: tiles
        self.camera_y = 0
        self.camera_zoom = 2
        self.images = self._get_images_in_directory(
            f"{PATH}graphics{DIR_SEPARATOR}", f"{PATH}graphics{DIR_SEPARATOR}")

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def main(self):
        clock = pygame.time.Clock()
        while self.running:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                self.handle_event(event)

            for chunk in self.chunks:
                chunk.render(self.screen, self.images, self.camera_x, 
                             self.camera_y, self.camera_zoom)

            pygame.display.flip()
            clock.tick(60)

    def _get_images_in_directory(self, path: str, 
                                 original_path: str) -> list[pygame.Surface]:
        os.chdir(path)
        files = os.listdir(os.getcwd())

        images = {}
        for file in files:
            path_here = path+file

            if not os.path.isfile(path_here):
                images.update(self._get_images_in_directory(
                    path_here+DIR_SEPARATOR, original_path))
                continue

            if is_valid_image(path_here):
                relative_path = path_here[len(original_path):]
                id_ = "/".join(relative_path.split(DIR_SEPARATOR))
                images[id_] = pygame.image.load(path_here).convert_alpha()

        return images
    
    def _load_world_data(self) -> list[Chunk]:
        chunks = []
        with open(f"data{DIR_SEPARATOR}world.json", "r") as file:
            data = json.load(file)
            for chunk_data in data:
                chunks.append(Chunk(**chunk_data))
                print(chunks[-1].x_pos, chunks[-1].y_pos, chunks[-1].tiles)

        return chunks


game = Game()
game.main()

pygame.quit()

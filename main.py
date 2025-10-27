import os
import platform
import pygame

from util import is_valid_image


pygame.init()
DIR_SEPARATOR = "/"
if platform.system == "Windows":
    DIR_SEPARATOR = "\\"
PATH = DIR_SEPARATOR.join(__file__.split(DIR_SEPARATOR)[:-1]) + DIR_SEPARATOR
print(PATH)


class Game:
    def __init__(self):
        # self.player = Player()
        # self.chunks = 
        self.running = True
        self.resolution = (1280, 720)
        self.screen = pygame.display.set_mode(self.resolution)
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

            pygame.display.flip()
            clock.tick(60)

    def _get_images_in_directory(self, path, original_path):
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


game = Game()
game.main()

pygame.quit()

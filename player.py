import pygame


FRAMES_PER_IMAGE = 10

class Player:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.animation = "stand_left"
        self.animation_frames_left = FRAMES_PER_IMAGE
        self.animation_length = 6
        self.current_animation_image = 0

    def tick(self):
        self.animation_frames_left -= 1
        if self.animation_frames_left == 0:
            self.current_animation_image += 1
            self.animation_frames_left = FRAMES_PER_IMAGE

        if self.current_animation_image == self.animation_length:
            self.current_animation_image = 0
    
    def render(self, screen: pygame.Surface, images,
               camera_x: int, camera_y: int, camera_zoom: int):
        
        TILE_SIZE = 16 * camera_zoom
        screen_size = screen.get_size()
        image = images[self._get_animation_image_id()]
        image = pygame.transform.scale_by(image, camera_zoom)

        # in-game coordinates, measured in tiles
        x = self.x_pos - camera_x
        y = self.y_pos - camera_y

        # convert to pixel coordinates
        x = TILE_SIZE*x + screen_size[0]//2 - image.get_width()//2
        y = TILE_SIZE*y + screen_size[1]//2 - image.get_height()//2

        screen.blit(image, (x, y))

    def _get_animation_image_id(self):
        base = self._get_animation_image_offset()
        return f"player/player_{base+self.current_animation_image}.png"

    def _get_animation_image_offset(self):
        match self.animation:
            case "stand_down": return 0
            case "stand_left": return 60
            case "stand_right": return 6
            case "stand_up": return 12

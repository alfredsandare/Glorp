import pygame

pygame.init()

path = "/".join(__file__.split("/")[:-1])
player_images = []
for i in range(60):
    image = pygame.image.load(f"{path}/graphics/player/player_{i}.png")
    player_images.append(pygame.transform.scale_by(image, 4))

seq_id = 9
sequence = player_images[6*seq_id:6*(seq_id+1)]
FRAMES_PER_IMG = 8

screen = pygame.display.set_mode((400, 300))

frames_left = FRAMES_PER_IMG
current_img = 0
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(sequence[current_img], (200, 150))
    frames_left -= 1
    if frames_left == 0:
        frames_left = FRAMES_PER_IMG
        current_img += 1
        if current_img == 6:
            current_img = 0


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
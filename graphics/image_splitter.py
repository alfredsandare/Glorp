from PIL import Image
import os

path = "/".join(__file__.split("/")[:-1])
print(path)
image = Image.open(path + "/Cute_Fantasy_Free/Player/Player.png")

image_data = image.getdata()

SIZE = 32
X, Y = 6, 10

i=0
for y in range(Y):
    for x in range(X):
        pixels = []
        for j in range(SIZE):
            start = X*SIZE**2*y + SIZE*x + X*SIZE*j
            pixels.extend([image_data[start+k] for k in range(SIZE)])

        new_image = Image.new("RGBA", (SIZE, SIZE))
        new_image.putdata(pixels)
        print(j)
        new_image.save(f"{path}/player/player_{i}.png")

        i+=1
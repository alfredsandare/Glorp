from PIL import Image


def is_valid_image(file_name):
    try:
        with Image.open(file_name) as img:
            img.verify()
            return True
    except (IOError, SyntaxError):
        return False

def rectangles_overlap(r1_x1, r1_y1, r1_x2, r1_y2, r2_x1, r2_y1, r2_x2, r2_y2):
    return r1_x1 < r2_x2 and r1_x2 > r2_x1 and r1_y1 < r2_y2 and r1_y2 > r2_y1

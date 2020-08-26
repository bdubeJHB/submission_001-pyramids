def get_shape():
    shapes = ["pyramid", "square", "triangle", "kite", "heart", "Octagon"]

    while 1:
        try:
            shape = input("Shape?: ")
            shape = shape.strip()
            shape = shape.lower()
            if shape and shape in shapes:
                break
        except EOFError:
            return None

    return shape


def get_height():
    height = "0"

    while int(height) > 80 or int(height) < 1:
        height = input("Height?: ").strip()
        if not height.isdigit():
            height = "0"

    return int(height)


def draw_pyramid(height, outline):
    if outline and height > 2:
        y = 0
        while y < height:
            print(' ' * (height - y - 1), end = '')
            if y == height - 1:
                print('*' * (height * 2 - 2), end = '')
            elif y:
                print('*', end = '')
                print(' ' * (y * 2 - 1), end = '')

            print('*')
            y += 1
            continue
    else:
        y = 1
        while y <= height:
            print(' ' * (height - y), end = '')
            print('*' * (2 * y - 1))
            y += 1


def draw_square(height, outline):
    x = 1

    if outline and height > 2:
        while x <= height:
            if x > 1 and x != height:
                print('*' + (' ' * (height - 2)) + '*')
            else:
                print('*' * height)
            x += 1
    else:
        while x <= height:
            print('*' * height)
            x += 1


def draw_triangle(height, outline):
    x = 1

    if outline and height > 2:
        while x <= height:
            if x < 3 or x == height:
                print('*' * x)
            elif x < height:
                print('*' + (' ' * (x - 2)) + '*')
            x += 1
    else:
        while x <= height:
            print('*' * x)
            x += 1


def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height, outline)
    if shape == "square":
        draw_square(height, outline)
    if shape == "triangle":
        draw_triangle(height, outline)
    if shape == "kite":
        draw_kite(heigh, outline)
    if shape == "heart":
        draw_heart(height, outline)
    if shape == "octagon":
        draw_octagon(height, outline)


def get_outline():
    outline = "F"

    while 1:
        outline = input("Outline only? (y/N): ")

        outline = outline.strip()
        outline = outline.lower()

        if outline == 'y':
            return True

        return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)




# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    return 'pyramid'


# TODO: Step 1 - get height (it must be int!)
def get_height():
    return 0


# TODO: Step 2
def draw_pyramid(height, outline):
    print('pyramid')


# TODO: Step 3
def draw_square(height, outline):
    print('square')


# TODO: Step 4
def draw_triangle(height, outline):
    print('triangle')


# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    draw_pyramid(height, outline)


# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    return False


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)


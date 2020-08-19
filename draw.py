

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shapes = ["pyramid", "square", "triangle"]

    while 1:
        shape = input("Shape?: ").lower()
        if shape or shape in shapes:
            break

    return shape


# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = "0"

    while int(height) > 80 or int(height) < 1:
        height = input("Height?: ")
        if not height.isdigit():
            height = "0"

    return int(height)


# TODO: Step 2
def draw_pyramid(height, outline):
    i = 1
    string = ""

    while i < height:
        j = 1
        while j < (height * 2) - 1:
            if i - height == 0:
                string += "*"
            else:
                string += " "
            j += 1

        string += "\n"
        i += 1
    print(string)


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


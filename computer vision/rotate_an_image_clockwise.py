def rotate_clockwise(image):
    height = len(image)
    width = len(image[0])

    output = [
        [0] * height
        for _ in range(width)
    ]

    for r in range(height):
        for c in range(width):
            output[c][height-1-r] = image[r][c]         

    return output
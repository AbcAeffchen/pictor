

def check_rgb_format(rgb_string):
    """
    TODO
    :param rgb_string:
    :return: bool
    """

    if rgb_string[0] != "#" or len(rgb_string) != 7:
        return False

    for c in rgb_string.upper()[1:]:
        if c not in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}:
            return False

    return True


def rgb_to_cmyk(rgb_string):
    """
    TODO
    :param rgb_string:
    :return: (c, y, m, k) A tuple of floats in [0,1]
    """

    r = int(rgb_string[1:3], 16) / 255
    g = int(rgb_string[3:5], 16) / 255
    b = int(rgb_string[5:7], 16) / 255

    k = max(r, g, b)
    c = (1 - r - k) / (1 - k)
    m = (1 - g - k) / (1 - k)
    y = (1 - b - k) / (1 - k)

    return c, y, m, k

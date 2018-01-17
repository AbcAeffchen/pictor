from math import fmod


def check_rgb_format(rgb_string):
    """
    Checks if rgb_string is actually a rgb string formatted as #[0-9a-fA-F]{6}
    :param rgb_string:
    :return: bool
    """

    if rgb_string[0] != "#" or len(rgb_string) != 7:
        return False

    for c in rgb_string.upper()[1:]:
        if c not in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}:
            return False

    return True


def rgb_to_cmyk(r, g, b):
    """
    Converts a RGB color tuple to a CMYK color tuple.
    :param g: int in [0, 255]
    :param r: int in [0, 255]
    :param b: int in [0, 255]
    :return: (c, y, m, k) A tuple of floats in [0,1]
    """

    r = r / 255
    g = g / 255
    b = b / 255

    k = 1 - max(r, g, b)
    c = (1 - r - k) / (1 - k)
    m = (1 - g - k) / (1 - k)
    y = (1 - b - k) / (1 - k)

    return c, m, y, k


def rgb_str_to_tuple(rgb_string):
    return int(rgb_string[1:3], 16), int(rgb_string[3:5], 16), int(rgb_string[5:7], 16)


def cmyk_to_rgb(cmyk):
    """
    Converts a CMYK color to a RGB color as tuple of integers in [0, 255]
    :param cmyk: CMYK color (as tuple)
    :return: (r,g,b) RGB color  as tuple of integers in [0, 255]
    """

    r = int(255 * (1-cmyk[0]) * (1-cmyk[3]))
    g = int(255 * (1-cmyk[1]) * (1-cmyk[3]))
    b = int(255 * (1-cmyk[2]) * (1-cmyk[3]))

    return r, g, b


def hsv_to_rgb(h, s, v):
    """
    Generates an rgb color tuple from a hsv color tuple
    :param h: hue number in [0, 360]
    :param s: Saturation float in [0,1]
    :param v: Value float in [0,1]
    :return: rgb tuple
    """
    c = s * v
    h_tmp = h / 60.0

    x = c * (1 - abs(fmod(h_tmp, 2) - 1))

    if 0 <= h_tmp < 1:
        r1, g1, b1 = c, x, 0
    elif 1 <= h_tmp < 2:
        r1, g1, b1 = x, c, 0
    elif 2 <= h_tmp < 3:
        r1, g1, b1 = 0, c, x
    elif 3 <= h_tmp < 4:
        r1, g1, b1 = 0, x, c
    elif 4 <= h_tmp < 5:
        r1, g1, b1 = x, 0, c
    else:
        r1, g1, b1 = c, 0, x

    m = v - c
    return int(255 * (r1 + m)), int(255 * (g1 + m)), int(255 * (b1 + m))

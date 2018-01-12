

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


def rgb_to_cmyk(rgb_string):
    """
    Converts a rgb string to a tuple representing a CMYK color.
    :param rgb_string:
    :return: (c, y, m, k) A tuple of floats in [0,1]
    """

    r = int(rgb_string[1:3], 16) / 255
    g = int(rgb_string[3:5], 16) / 255
    b = int(rgb_string[5:7], 16) / 255

    # print(r,g,b)

    k = 1 - max(r, g, b)
    c = (1 - r - k) / (1 - k)
    m = (1 - g - k) / (1 - k)
    y = (1 - b - k) / (1 - k)

    # print(c,m,y,k)

    return c, m, y, k


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

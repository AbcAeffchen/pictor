import argparse
import helpers
import random


class Pictor:

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="Generate pixel art as vector image.")

        parser.add_argument("-c", "--color", type=str, metavar="#RGB",
                            help="The color value as #rgb.")
        parser.add_argument("-bg", "--background", type=str, default="#FFFFFF", metavar="#RGB",
                            help="The background color value as #rgb.")
        parser.add_argument("-b", "--border", nargs=2, type=str, default=["0", "#000000"], metavar=("width", "#RGB"),
                            help="Width and color of the border between pixels.")
        parser.add_argument("-d", "--dim", nargs=2, type=int, default=[15, 10], metavar=("width", "height"),
                            help="dimension in pixels as width and height.")
        parser.add_argument("-n", "--num_shadings", type=int, default=10, metavar="num",
                            help="The number of shades used in the image.")
        parser.add_argument("-s", "--scale", type=int, default=40, metavar="int",
                            help="The size of a pixel.")
        parser.add_argument("-sp", "--sub-pixels", type=int, default=0, metavar="int",
                            help="The number of times a pixel can be split into 4 sub pixels")
        parser.add_argument("-spp", "--sub-pixels-probability", type=float, default=0.1, metavar="float",
                            help="The probability a pixel or sub pixel is split into sub pixels.")
        parser.add_argument("-r", "--radius", type=int, default=0, metavar="int",
                            help="Pixel corner radius.")
        parser.add_argument("-rb", "--rainbow", action="store_true",
                            help="Use rainbow colors instead of a fixed color.")
        parser.add_argument("-o", "--out", type=str, default="out.svg", metavar="path",
                            help="The path to the output file.")
        parser.add_argument("-v", "--verbose", action="store_true",
                            help="Print additional outputs")
        parser.add_argument("--version", action="version", version="Pictor 0.1")

        args = parser.parse_args()

        if args.verbose:
            print(args)

        # validate inputs
        if args.color is not None and not helpers.check_rgb_format(args.color):
            print("Color needs to be in RGB format")
            return False, None

        if args.background is not None and not helpers.check_rgb_format(args.background):
            print("Background color needs to be in RGB format")
            return False, None

        if args.num_shadings < 1:
            print("The number of shades needs to be at least 1")
            return False, None

        if args.scale < 1:
            print("The scale needs to be positive.")
            return False, None

        args.border[0] = int(args.border[0])

        return True, args

    def __init__(self):
        # parse arguments
        valid, self.args = self.parse_arguments()

        if not valid:
            quit(1)

        # depending on the arguments create the right image
        dims = self.get_image_dimensions()
        image = self.create_random_image(dims, self.args.color)

        self.export_svg(image, dims)

    def get_image_dimensions(self):
        """
        Calculates the dimensions of the image in pixels depending on the arguments.
        :return:
        """

        # todo pixel size needs to be adjusted if "pixels off the grid" are introduced.
        pixel_size = 2 ** self.args.sub_pixels
        return {"x": self.args.dim[0] * pixel_size,
                "y": self.args.dim[1] * pixel_size,
                "pixel_size": pixel_size}

    def get_contrasts(self, cmyk_color):
        contrast_range_factor = {"min": 0.5, "max": max(1, 0.9 / cmyk_color[3])}
        contrast_step_size = (contrast_range_factor["max"] - contrast_range_factor["min"]) / self.args.num_shadings

        return [cmyk_color[3] * (contrast_range_factor["min"] + step * contrast_step_size) for step in
                range(0, self.args.num_shadings)]

    def create_random_image(self, dims, rgb_color):
        """

        :param dims: Image dimensions
        :param rgb_color: A color in RGB format.
        :return:
        """

        image = {"background": helpers.rgb_str_to_tuple(self.args.background),
                 "pixels": []}

        if not self.args.rainbow :
            cmyk_color = helpers.rgb_to_cmyk(*helpers.rgb_str_to_tuple(rgb_color))
            contrasts = self.get_contrasts(cmyk_color)

        for x in range(0, dims["x"], dims["pixel_size"]):
            if self.args.rainbow:
                cmyk_color = helpers.rgb_to_cmyk(*helpers.hsv_to_rgb(360.0 / dims["x"] * x, 0.75, 0.9))
                contrasts = self.get_contrasts(cmyk_color)

            for y in range(0, dims["y"], dims["pixel_size"]):
                image["pixels"].extend(self.get_pixel(cmyk_color, contrasts, x, y, dims["pixel_size"]))

        return image

    def get_pixel(self, cmyk_color, contrasts, x, y, pixel_size):
        if pixel_size > 1 and random.random() <= 0.2:
            sub_pixel_size = pixel_size / 2

            return [*self.get_pixel(cmyk_color, contrasts, x, y, sub_pixel_size),
                    *self.get_pixel(cmyk_color, contrasts, x + sub_pixel_size, y, sub_pixel_size),
                    *self.get_pixel(cmyk_color, contrasts, x, y + sub_pixel_size, sub_pixel_size),
                    *self.get_pixel(cmyk_color, contrasts, x + sub_pixel_size, y + sub_pixel_size, sub_pixel_size)]
        else:
            return [{"x": x, "y": y, "size": pixel_size, "radius": self.args.radius * pixel_size,
                    "color": helpers.cmyk_to_rgb((*cmyk_color[:3], random.choice(contrasts)))}]

    def export_svg(self, image, dims):
        """
        Writes image to file.
        :param image: Image dictionary
        :param dims: Image dimensions dictionary
        """

        f = open(self.args.out, 'w')

        scale = self.args.scale

        # open file
        f.write("<svg viewbox=\"0 0 {0} {1}\" width=\"{0}\" height=\"{1}\" xmlns=\"http://www.w3.org/2000/svg\">"
                .format(dims["x"] * scale, dims["y"] * scale))

        # add background
        f.write("<rect width=\"{0}\" height=\"{1}\" x=\"0\" y=\"0\" "
                "style=\"fill: rgb({2},{3},{4}); stroke-width: 0\"/>"
                .format(dims["x"] * scale, dims["y"] * scale, *image["background"]))

        # write pixels
        for pixel in image["pixels"]:
            f.write("<rect height=\"{0}\" width=\"{0}\" x=\"{1}\" y=\"{2}\" "
                    .format(pixel["size"] * scale, pixel["x"] * scale, pixel["y"] * scale)
                    + ("rx=\"{0}\" ry=\"{0}\" ".format(pixel["radius"]) if pixel["radius"] > 0 else "")
                    + "style=\"fill: rgb({0},{1},{2});".format(*pixel["color"])
                    + ("stroke-width:{0};stroke: rgb({1},{2},{3})"
                        .format(self.args.border[0], *helpers.rgb_str_to_tuple(self.args.border[1]))
                        if self.args.border[0] > 0 else "")
                    + "\"/>")

        # close file
        f.write("</svg>")
        f.close()

# linux needs to mask the #
# python3 pictor/core.py -v -d 30 20 -c \#5fd7dd -n 10 -s 40 -r 10 -bg \#888888 -b 1 \#FFFFFF
Pictor()

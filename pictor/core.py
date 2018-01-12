import argparse
import helpers
import random


class Pictor:

    def parse_arguments(self):
        parser = argparse.ArgumentParser(description="Generate pixel art as vector image.")

        parser.add_argument("-c", "--color", type=str,
                            help="The color value as #rgb.")
        parser.add_argument("-d", "--dim", nargs=2, type=int, default=[10, 15],
                            help="dimension in pixels as width and height.")
        parser.add_argument("-o", "--out", type=str, default="out.svg",
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

        return True, args

    def __init__(self):
        # parse arguments
        valid, self.args = self.parse_arguments()

        if not valid:
            quit(1)

        # depending on the arguments create the right image
        dims = self.get_image_dimensions()
        image = self.create_random_image(dims, "#ABCABC")

        self.export_svg(image, dims)

    def get_image_dimensions(self):
        """
        Calculates the dimensions of the image in pixels depending on the arguments.
        :return:
        """

        # todo pixel size needs to be adjusted if the subpixels and pixels off the grid are introduced.
        return {"x": self.args.dim[0],
                "y": self.args.dim[1],
                "pixel_size": 1}

    def create_random_image(self, dims, rgb_color):
        """

        :param dims: Image dimensions
        :param rgb_color: A color in RGB format.
        :return:
        """

        cmyk_color = helpers.rgb_to_cmyk(rgb_color)

        image = {"background": "#FFFFF",  # todo make background optional
                 "pixels": []}

        contrast_ragne_factor = {"min": 0.5, "max": max(1, 0.9 / cmyk_color[3])}
        # todo adjust number of steps, currently fixed to 10
        contrast_step_size = (contrast_ragne_factor["max"] - contrast_ragne_factor["min"]) / 10

        contrasts = [cmyk_color[3] * (contrast_ragne_factor["min"] + step * contrast_step_size) for step in
                     range(0, 10)]

        for x in range(0, dims["x"]):
            for y in range(0, dims["y"]):
                image["pixels"].append({"x": x, "y": y, "size": dims["pixel_size"],
                                        "color": helpers.cmyk_to_rgb((cmyk_color[0], cmyk_color[1], cmyk_color[2],
                                                                      random.choice(contrasts)
                                                                      ))
                                        })

        return image

    def export_svg(self, image, dims):
        """

        :param image:
        :return:
        """

        f = open(self.args.out, 'w')



        # open file
        f.write("<svg viewbox=\"0 0 {1} {0}\" xmlns=\"http://www.w3.org/2000/svg\">".format(dims["x"] * 32, dims["y"] * 32))

        # write pixels
        for pixel in image["pixels"]:
            f.write("<rect height=\"{0}\" width=\"{0}\" x=\"{2}\" y=\"{1}\" style=\"fill: rgb({3},{4},{5}); stroke-width: 0\"/>"
                    .format(pixel["size"] * 32, pixel["x"] * 32, pixel["y"] * 32, pixel["color"][0], pixel["color"][1], pixel["color"][2]
                            )
                    )

        # close file
        f.write("</svg>")
        f.close()


        # todo image is a list of pixels. write them into a file.


Pictor()

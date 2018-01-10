import argparse


class Pictor:
    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(description="Generate pixel art as vector image.")

        parser.add_argument("-c", "--color", help="The color value as #rgb.")
        parser.add_argument("-o", "--out", help="The path to the output file.")
        parser.add_argument("-v", "--verbose", help="Print additional outputs", action="store_true")
        parser.add_argument("--version", action="version", version="Pictor 0.1")

        return parser.parse_args()

    def __init__(self):
        self.args = self.parse_arguments()
        if self.args.verbose:
            print("Verbose is on")


Pictor()

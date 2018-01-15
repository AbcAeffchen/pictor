# Pictor
Generate pixel art as vector image.

![Alt text](/examples/example-0.svg "example-0")
![Alt text](/examples/example-1.svg "example-1")

## Usage

```
usage: core.py [-h] [-c COLOR] [-bg BACKGROUND] [-b BORDER BORDER]
               [-d DIM DIM] [-n NUM_SHADINGS] [-s SCALE] [-r RADIUS] [-o OUT]
               [-v] [--version]

Generate pixel art as vector image.

optional arguments:
  -h, --help            show this help message and exit
  -c COLOR, --color COLOR
                        The color value as #rgb.
  -bg BACKGROUND, --background BACKGROUND
                        The background color value as #rgb.
  -b BORDER BORDER, --border BORDER BORDER
                        Width and color of the border between pixels.
  -d DIM DIM, --dim DIM DIM
                        dimension in pixels as width and height.
  -n NUM_SHADINGS, --num_shadings NUM_SHADINGS
                        The number of shades used in the image.
  -s SCALE, --scale SCALE
                        The size of a pixel.
  -r RADIUS, --radius RADIUS
                        Pixel corner radius.
  -o OUT, --out OUT     The path to the output file.
  -v, --verbose         Print additional outputs
  --version             show program's version number and exit
```

## Features

- Random pixels of different shades of a single fixed color.
- (planned) Random pixels of different shades of the full spectrum.
- (planned) Colormap: Use a Bitmap image to get the color from.
- (planned) Adjustable shade intensity.
- (planned) Adjustable randomness.
    - (planned) light to dark and other way around.
    - (planned) light to dark to light and other way around.
- Adjustable image size in terms of numbers of pixels per row and column.
- (planned) Dynamic resolution: split some pixels into subpixels.
    - (planned) Adjustable randomess for subpixels.
    - (planned) Adjustable places (top, bottom, one or more coordinates in the image).
    - (planned) Subpixels that leave the grid.
- (planned) Pixels/Subpixels that leave the grid (random, adjustable)
- Adjustable pixel boarders (color, thickness)
- Adjustable image background color
- Round Pixel corners

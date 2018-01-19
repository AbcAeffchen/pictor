# Pictor
Generate pixel art as vector image.

![Alt text](/examples/example-0.svg "example-0")
![Alt text](/examples/example-1.svg "example-1")
![Alt text](/examples/example-2.svg "example-1")

## Usage

```
usage: core.py [-h] [-c COLOR] [-bg BACKGROUND] [-b BORDER BORDER]
               [-d DIM DIM] [-n NUM_SHADINGS] [-s SCALE] [-sp SUB_PIXELS]
               [-spp SUB_PIXELS_PROBABILITY] [-r RADIUS] [-rb] [-o OUT] [-v]
               [--version]

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
  -sp SUB_PIXELS, --sub-pixels SUB_PIXELS
                        The number of times a pixel can be split into 4 sub
                        pixels
  -spp SUB_PIXELS_PROBABILITY, --sub-pixels-probability SUB_PIXELS_PROBABILITY
                        The probability a pixel or sub pixel is split into sub
                        pixels.
  -r RADIUS, --radius RADIUS
                        Pixel corner radius.
  -rb, --rainbow        Use rainbow colors insead of a fixed color.
  -o OUT, --out OUT     The path to the output file.
  -v, --verbose         Print additional outputs
  --version             show program's version number and exit
```

## Features

- Random pixels of different shades of a single fixed color.
- Random pixels of different shades of the full spectrum.
- (planned) Colormap: Use a Bitmap image to get the color from.
- (planned) Adjustable shade intensity.
- (planned) Adjustable randomness.
    - (planned) light to dark and other way around.
    - (planned) light to dark to light and other way around.
- Adjustable image size in terms of numbers of pixels per row and column.
- Dynamic resolution: split some pixels into subpixels.
    - Adjustable randomess for subpixels.
    - (planned) Adjustable places (top, bottom, one or more coordinates in the image).
    - (planned) Subpixels that leave the grid.
- (planned) Pixels/Subpixels that leave the grid (random, adjustable)
- Adjustable pixel boarders (color, thickness)
- Adjustable image background color
- Round Pixel corners

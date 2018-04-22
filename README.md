# Pictor
Generate pixel art as vector image.

![Alt text](/examples/example-0.svg "example-0")
![Alt text](/examples/example-1.svg "example-1")
![Alt text](/examples/example-2.svg "example-1")

## Usage

```
usage: core.py [-h] [-c #RRGGBB] [--contrast min max] [-bg #RRGGBB]
               [-b width #RRGGBB] [-d width height] [-n num] [-s int]
               [-sp int] [-spp float] [-r int] [-rb] [-o path] [-v]
               [--version]

Generate pixel art as vector image.

optional arguments:
  -h, --help            show this help message and exit
  -c #RRGGBB, --color #RRGGBB
                        The color value as #rrggbb.
  --contrast min max    The contrast range of the pixels.
  -bg #RRGGBB, --background #RRGGBB
                        The background color value as #rgb.
  -b width #RRGGBB, --border width #RRGGBB
                        Width and color of the border between pixels.
  -d width height, --dim width height
                        dimension in pixels as width and height.
  -n num, --num_shadings num
                        The number of shades used in the image.
  -s int, --scale int   The size of a pixel.
  -sp int, --sub-pixels int
                        The number of times a pixel can be split into 4 sub
                        pixels
  -spp float, --sub-pixels-probability float
                        The probability a pixel or sub pixel is split into sub
                        pixels.
  -r int, --radius int  Pixel corner radius.
  -rb, --rainbow        Use rainbow colors instead of a fixed color.
  -o path, --out path   The path to the output file.
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
- (planned) Small svg files without compression.
- (planned) support gzipped output. (can directly displayed by chrome)

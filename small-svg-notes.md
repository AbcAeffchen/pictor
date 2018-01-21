# Building small svg pixel files

A svg pixel file contains only objects of type `rect`. A minimal object is
```
<rect height="dd" width="dd" x="ddd" y="ddd" style="fill: rgb(ddd,ddd,ddd);stroke-width:d"/>
```

It has about 89 - 97 characters. `ddd` is a number and most likely has between 1 and 4 digits.

They can have different combinations of the following attributes:

1. ` rx="dd" ry="dd"` where `d` is a digit. (16 characters)
2. `;stroke: rgb(ddd,ddd,ddd)` (25 characters)
3. more options soon.

## Minify Possibilities

### Styles
Since the generated pixel differ only little relativ to the number of pixels, styles can safe some bytes.

Add

- `<style></style>` one per file. (15 bytes)
- `.r{stroke-width:0;stroke:rgb(ddd,ddd,ddd);}` one per file (43 bytes) or to each style.
This depends on the number of pixels, since for each pixel 2 extra bytes are needed to add this class.
- `.cdd{fill:rgb(ddd,ddd,ddd)}` per color, where `dd` is a counter. (27 bytes per color/shade)

### Symbols
There are only a few different pixels namely one per color/shade. So they
can defined once with symbols and then used multiple times in different scales.

Add

TODO defs + ids auf die refs sollte immer kürzer sein als symbol. wenn width einmal gesetzt ist brauch ich das bei use wohl nicht nochmal => TESTEN!!!

```
<symbol id="rdd">
    <rect height="dd" width="dd" x="ddd" y="ddd" style="fill: rgb(ddd,ddd,ddd);stroke-width:d"/>
</symbol>
```
for each color/shade and then use
```

```

## Theoretical Comparison:

Number of Pixels: 30 * 20 = 600

| options | naive | style | symbol | style + symbol
---------------------------------------------------
| no options |


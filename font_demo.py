from itertools import chain
import sys

from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

ttf = TTFont('222.ttf', 0, verbose=0, allowVID=0,
                ignoreDecompileErrors=True,
                fontNumber=-1)

chars = ([y for y in x.cmap.items()] for x in ttf["cmap"].tables)
print(list(chars))
# Two type of Module
# Built In Module (Internal Module) : direct import like import math, os etc.
# External Module : pip install

import math
import os # IDE shows the color of this module is blur beacuse we imported but not in use, means this is unused module (when any module in use it show the color darker)

print(math.sqrt(25))
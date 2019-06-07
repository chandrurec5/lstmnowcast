import numpy as np
import os
import yaml
import logging
from collections import OrderedDict
from nowcasting.helpers.ordered_easydict import OrderedEasyDict as edict

__C = edict()
cfg = __C  # type: edict()

# Random seed
__C.MOVINGMNIST = edict()
__C.MOVINGMNIST.DIGIT_NUM = 3



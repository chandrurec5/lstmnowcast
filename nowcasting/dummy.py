import numpy as np
import os
import yaml
import logging
from collections import OrderedDict
from nowcasting.helpers.ordered_easydict import OrderedEasyDict as edict

C = edict()
cfg = C  # type: edict()

# Random seed
C.MOVINGMNIST = edict()
C.MOVINGMNIST.DIGIT_NUM = 3



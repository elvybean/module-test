# INNER ##################################################################
# inside a seperate directory and not in the same directory as the package
##########################################################################
# Below is needed for scripts not in the same directory as a package
##########################################################################

import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)

##########################################################################

import num_lib

num_lib.One()
num_lib.Two()
num_lib.Three()

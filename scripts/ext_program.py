# this MUST be inside a seperate directory to module_test but still in the same root directory as module_test
# Below is the specific code needed for py scripts not in the same directory as module_test to access it
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)
#####

import module_test

module_test.functionOne()
module_test.functionTwo()
module_test.functionThree()
module_test.callingThree()

from . import script4 as sc4
from . import script5 as sc5


def functionThree():
    print("This text output is from functionThree in script3")


def callingThree():
    print("Calling functions from script4 and script5 but within script3: ")
    sc4.functionFour()
    sc5.functionFive()
    print("This text output is from callingThree in script3")

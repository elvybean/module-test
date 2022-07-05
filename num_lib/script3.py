from . import script1 as One
from . import script2 as Two


def Three():
    print("This text output is from the module script3's defThree function")
    print("now calling functions from script1 and script2 but within script3")
    Two.Four()
    One.Five()

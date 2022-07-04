
def Four():
    print("This text output is from defFour function")


def Five():
    print("This text output is from defFive function")


def Three():
    print("This text output is from the module script3's defThree function")
    print("now calling functions from within script3")
    Four()
    Five()

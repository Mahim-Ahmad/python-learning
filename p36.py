#methode overiding

class phone:
    def __init__(self):
        print("You can call")
    

class samsung(phone):

    def __init__(self):
        super().__init__()
        print("You can take phote")

s=samsung()
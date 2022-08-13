class Theory:

    def __init__(self):
        print("this is Theory")

class Sessional:
    def __init__(self):

        print("this is Sessional")


class Result(Theory,Sessional):

    def __init__(self):
        super().__init__()

        print("this is Result")


r=Result()
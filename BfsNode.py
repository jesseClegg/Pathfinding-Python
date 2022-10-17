from io import StringIO


class BfsNode:
    def __init__(self, i, j, distance ):
        self.i=i
        self.j=j
        self.distance=distance

    def __str__(self):
        #print("inside to string!!")
        myString = str(self.i)+str(self.j)
        return myString



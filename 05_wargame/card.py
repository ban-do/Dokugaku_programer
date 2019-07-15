class Card:

    #柄
    suits = ["spades", "hearts", "diamonds", "club"]

    #値
    values = [None,None,
              "2","3","4","5","6","7","8","9",
              "10","Jack","Queen","King","Ace"]

    #initialize
    def __init__(self,v ,s):

        #index value を渡している
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        elif self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        elif self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        else:
            return False

    def __repr__(self):
        v = self.values[self.value] + " of "\
            + self.suits[self.suit]
        return v

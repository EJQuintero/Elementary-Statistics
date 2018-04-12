#Probabilities problems

'''Question 1. A jar contains 2 blue marbels 3 red marbles, 7 green marbles and 10 white marbles:
A) If a marble is drawn from the jar at random, what is the probability that this marble is white?
B) What is the probability of picking 1 blue, and 1 red?'''

#Set up class marbels to get the population size define by user to leverage the capabilities later
class marbels:

    def __init__(self, b, r, g, w):
        self.b = b
        self.r = r
        self.g = g
        self.w = w

    def MarbelSum(self):
        total = self.b + self.r + self.g + self.w
        return total

#==================================================

#Part A. Calculate the probability of drawing a particular color first
class color(marbels):

    def __init__(self, b, r, g, w, color):
        super().__init__(b, r, g, w)
        self.color = color

    def getColor(self):
        c = self.color.lower()
        if c == 'blue':
            return (self.b / self.MarbelSum())
        elif c == 'red':
            return (self.r / self.MarbelSum())
        elif c == 'green':
            return (self.g / self.MarbelSum())
        else:
            return (self.w / self.MarbelSum())

    def __str__(self):
        return 'The possibility of color {} is {}'.format(self.color, self.getColor())

#=====================================================

#Part B. Calculate the probability of 1 blue, and 1 red marbel.
class spec(color):

    def __init__(self, b, r, g, w, color,color2):
        super().__init__(b, r, g, w, color)
        self.color2 = color2

    def prob2(self):
        c2 = self.color2.lower()
        if c2 == self.color.lower():
            if c2 == 'blue':
                return (self.b - 1) / (self.MarbelSum() - 1)
            elif c2 == 'red':
                return (self.r - 1) / (self.MarbelSum() - 1)
            elif c2 == 'green':
                return (self.g - 1) / (self.MarbelSum() - 1)
            else:
                return (self.w - 1) / (self.MarbelSum() - 1)
        else:
            if c2 == 'blue':
                return (self.b)/ (self.MarbelSum() - 1)
            elif c2== 'red':
                return (self.r) / (self.MarbelSum() - 1)
            elif c2 == 'green':
                return (self.g) / (self.MarbelSum() - 1)
            else:
                return (self.w) / (self.MarbelSum() - 1)

    def combine(self):
        return self.getColor() + self.prob2()

    def __str__(self):
        return 'The possibility of picking {} and {} is {}'.format(self.color, self.color2, self.combine())

if __name__ == '__main__':
    d = color(2,3,7,10,'White')
    print(d)
    j = spec(2,3,7,10,'Blue','Red')
    print(j)
'''
class mean:

    def __init__(self, *args):
        self.arg = args

    def getObservations(self):
        observations = []
        for item in self.arg:
            observations.append(item)
        return observations

    def getSum(self):
        total = sum(self.getObservations())
        return total

    def n(self):
        n = len(self.getObservations())
        return n

    def calculateMean(self):
        mean = self.getSum() / self.n()
        return mean

    def __str__(self):
        return 'The mean (algebraic average) = {}'.format(self.calculateMean())

if __name__ == '__main__':
    d = mean(9.3,11,28.7,7.6,6.5,8.7,7.4,7.8,6.7,9.5)
    print(d)
'''
#=================================================================
'''
class median:

    def __init__(self, *args): #input as many observations as needed
        self.arg = args

    def getObservations(self): #converts observations into a list of numbers and sorts them in increasing order
        observations = []
        for item in self.arg:
            observations.append(item)
        observations.sort()
        return observations

    def n(self): #counts the number of observations (n)
        n = len(self.getObservations())
        return n

    def getMedian(self):
        if self.n() % 2 == 0: #calculates the median in an even number of observations
            meanCenter = int(self.n() / 2)
            n1 = self.getObservations()[meanCenter]
            n2 = self.getObservations()[meanCenter - 1] #index the two center numbers
            mean = (n1 + n2) / 2
            return mean
        else: #finds the median number (the number in the center of the sample/population)
            center = int(self.n() / 2)
            mean = self.getObservations()[center] #index the center number (median)
            return mean

    def __str__(self):
        return 'The median is {}'.format(self.getMedian())

if __name__ == '__main__':
    d = median(9.3,11,28.7,7.6,6.5,8.7,7.4,7.8,6.7,9.5)
    print(d)

'''
#===========================================================
'''
class mode:

    def __init__(self, *args):
        self.arg = args

    def getObservations(self):
        obaservations = []
        for item in self.arg:
            obaservations.append(item)
        obaservations.sort()
        return obaservations

    def n(self):
        n = len(self.getObservations())
        return n

    def getMode(self):
        counter = 1
        mod = []
        mode = []
        for i in self.getObservations():
            if i not in mod:
                mod.append(i)
        for j in self.getObservations():
            if j not in mode:
                mode = [{j:counter}]
            else:
                mode = [{j:counter+1}]

        return mode



    def __str__(self):
        return '{}'.format(self.getObservations())

if __name__ == '__main__':
    d = mode(9.3,11,28.7,7.6,6.5,8.7,7.4,7.8,6.7,9.5)
    print(d)
'''

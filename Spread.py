
class Range:

    def __init__(self, *args):
        self.arg = args

    def getObservations(self):
        observations = []
        for item in self.arg:
            observations.append(item)
        observations.sort()
        return observations

    def getRange(self):
        rang = self.getObservations()[-1] - self.getObservations()[0] #used index, could have also used min & max
        return rang

    def __str__(self):
        return 'The range is {}'.format(self.getRange())

if __name__ == '__main__':
    d = Range(6.5, 6.7, 7.4, 7.6, 7.8, 8.7, 9.3, 9.5, 11, 28.7)
    print(d)


#===============================================================

class SD:

    def __init__(self, *args):
        self.arg = args

    def getObservations(self):
        observations = []
        for item in self.arg:
            observations.append(item)
        observations.sort()
        return observations

    def getTotal(self):
        total = sum(self.getObservations())
        return total

    def n(self):
        n = len(self.getObservations())
        return n

    def calculateMean(self):
        mean = self.getTotal() / self.n()
        return mean

    def Suma(self):
        suma = 0
        for i in self.getObservations():
            suma += (i - self.calculateMean()) ** 2
        return suma

    def getSD(self):
        s2 = self.Suma() / (self.n() - 1)
        SD = s2 ** (1/2)
        return SD

    def __str__(self):
        return'mean = {}, and SD = {}'.format(self.calculateMean(),self.getSD())

#test
if __name__ == '__main__':
    d = SD(7.0,4.5,7.8,6.4,14.7,6.6,8)
    print(d)

#==========================================================

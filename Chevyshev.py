'''Making use of Chevyshev's Rule. User inputs mean, standard deviation, and either upper & lower limits, or percentage
of the sample, or maximum upper limit.'''

class Chevyshev:

    def __init__(self, mean, s, *args):
        self.mean = mean
        self.s = s
        self.arg = args

    def lst(self): #Step need to make turn the argument(s) into a list for processing later
        lst = list(self.arg)
        return lst

    def selection(self):
        if len(self.arg) > 1: #scenario 1, given upper and lower limits, determine percentage of sample
            low = 0
            high = 0
            for n in self.arg:
                low = self.arg[0]
                high = self.arg[1]
                if low < high:
                    pass
                else:
                    (low, high) = (high, low)
            x = self.mean - low
            k = x / self.s
            ans = 1 - (1 / k ** 2)
            return ans
        elif self.lst()[0] < 1 and self.lst()[0] > 0: #scenario 2, find the interval when a % of sample is given
            low = 0
            high = 0
            k = (1 / (1 - self.lst()[0]) ) ** 0.5
            low = round(self.mean - (k * self.s))
            high = round(self.mean + (k * self.s))
            return ('k = ',k, 'the intervals are',low, high)
        else: #scenario 3, find the percentage of students who had more than 400 (use max formula 1/k^2)
            k = (self.lst()[0] - self.mean) / self.s
            ans = 1 / k ** 2
            return (ans, 'k =', k)

    def __str__(self):
        return '{}'.format(self.selection())

if __name__ == '__main__':
    d = Chevyshev(646,14,0.84)
    print(d)

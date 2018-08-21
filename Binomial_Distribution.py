'''The formula for the Binomial Distribution is P(x) = nCx * p^x * q^(n-x), where:
n = the number of trials
x = the number of successful trials
p = the probability of success of each trial
q = the complement of p (1 - p). The value of q will be calculated within the function to simplify user input.

We will import the nCx function from the nCx module created in a different file within this repository.'''

from nCx import nCx

def P(n, x, p):
    q = 1 - p
    PofX = nCx(n, x) * (p**x) * q**(n - x)
    return format(PofX,'.4f')

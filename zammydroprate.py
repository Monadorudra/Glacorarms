#N is base drop rate, e.g. N=100 for enrage 0-19%
N=100
def zamorakdroprate(N):
    sum1 = 0.0
    sum2 = 0.0
    sum3 = 0.0
    for i in range(1, 11):
        sum1 = sum1 + i * (1 / N) * ((N - 1) / N) ** (i - 1)

    for i in range(1, N - 20 + 1):
        sum2 = sum2 + (i+10) * (1 / (N - 1)) * ((N - 1) / N) ** 10

    for i in range(1,1000000):
        sum3 = sum3+(i+10+N-20)* (((N - 1) / N) ** 10 * (19) * (1 / (N - 1)))*(1/20)*(19/20)**(i-1)

    return sum1+sum2+sum3

print('average number of kills until rare drop')
print(zamorakdroprate(N))

#sanity checking probability distribution
def checkprob(N):
    sum1 = 0.0
    sum2 = 0.0
    sum3 = 0.0
    for i in range(1, 11):
        sum1 = sum1 + (1 / N) * ((N - 1) / N) ** (i - 1)

    for i in range(1, N - 20+1):
        sum2 = sum2 +  (1 / (N - 1)) * ((N - 1) / N) ** 10

    #sum3 = (((N - 1) / N) ** 10 * (19) * (1 / (N - 1))) * 20 / 20
    for i in range(1,1000000):
        sum3 = sum3+(((N - 1) / N) ** 10 * (19) * (1 / (N - 1)))*(1/20)*(19/20)**(i-1)
    return sum1+sum2+sum3

print('should be 1 no matter what N is, provided N>=20')
print(checkprob(N))
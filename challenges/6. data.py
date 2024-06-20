import statistics

"""
A pharmaceutical company wants to know whether an experimental drug affects systolic blood pressure.
Fifteen randomly selected subjects were given the drug and, after sufficient time for the drug to have an impact,
their systolic blood pressures were recorded.
The data appears in a python list.

THE FOLLOWING POINTS MUST BE DONE USING SOME FUNCTIONS OF SOME MODULE, AND WITH ANOTHER FUNCTION THAT YOU BUILT,
THAT IS, IMITATE THE BEHAVIOUR OF THAT FUNCTION

1. Calculate the value of 'x bar' (sample mean) and the value of s (the sample standard deviation)

"""

data = [172, 140, 123, 130, 115, 148, 108, 129, 137, 161, 123, 152, 133, 128, 142]


print('With Statistics')
print('Tis is the mean')
print(statistics.mean(data))
print('This is standard deviation')
print(statistics.stdev(data))

# Yo haciendo funciones
print('Tis is the mean')


def media():
    suma = sum(data)
    med = suma / (len(data))
    return med


print(media())

print('This is standard deviation')
xbar = media()


def desest(su=0):
    for a in data:
        r = a - xbar
        su2 = r ** 2
        su = su + su2
    su4 = su / (len(data) - 1)
    su3 = su4 ** .5
    return su3


print(desest())

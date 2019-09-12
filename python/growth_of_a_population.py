"""
In a small town the population is p0=1000 at the beginning of a year.
The population regularly increases by 2 percent per year and moreover
50 new inhabitants per year come to live in the town.

How many years does the town need to see its population greater or equal
to p=1200 inhabitans?

More generally give parameters:
p0, percent, aug(inhabitans coming or leaving each year), 
p(population to surpass).

The function 'nb_year' should return 'n' number of entire years needed
to get a population greater or equal to 'p'.

'aug' is an integer, percent a positive or null number, p0 and p are
positive integers (>0).

Note: Don't forget to convert the percent parameter as a percentage in
the body of your function, if the parameter percent is 2 you have to 
convert it to 0.02
"""

# My Answer
def nb_year(p0, percent, aug, p):
    percent = percent / 100
    p1 = [p0 * (1 + percent) + aug]
    while p1[-1] < p:
        pn = p1[-1] * (1 + percent) + aug
        p1.append(pn)
    return len(p1)

# Best Answer
def nb_year(population, percent, aug, target):
    year = 0
    while population < target:
        population += population * percent / 100. + aug
        year += 1
    return year

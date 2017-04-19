import thinkstats2
import thinkplot
import nsfg
from math import sqrt


hist = thinkstats2.Hist([1, 2, 2, 3, 5])
print(hist)
print(hist.Freq(2), hist.Freq(4))
print(hist.Values())  # unsorted list of the values in the Hist

for val in sorted(hist.Values()):
    print(val, hist.Freq(val))
print()
for val, freq in hist.Items():
    print(val, freq)

thinkplot.Hist(hist)
# thinkplot.Show(xlable='value', ylabel='frequency')

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
hist = thinkstats2.Hist(live.birthwgt_lb, label='birthwgt_lb')
# thinkplot.Hist(hist)
# thinkplot.Show(xlabel='pounds', ylabel='frequency')

print()
for weeks, freq in hist.Smallest(10):  # 10 smallest values from histogram # Largest
    print(weeks, freq)

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]
first_hist = thinkstats2.Hist(firsts.prglngth)
other_hist = thinkstats2.Hist(others.prglngth)

width = 0.45
thinkplot.PrePlot(2)  # no of histograms we are planning to plot
thinkplot.Hist(first_hist, align='right', width=width)
thinkplot.Hist(other_hist, align='left', width=width)
# thinkplot.Show(xlabel='weeks', ylabel='frequency', xlim=[27, 46])

print(live.prglngth.mean())
print(live.prglngth.var())
print(live.prglngth.std())


def cohens_d(group1 ,group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1*var1 + n2*var2)/(n1 + n2)
    d = diff / sqrt(pooled_var)
    return d

print("cohen's d: ", cohens_d(firsts.prglngth, others.prglngth))

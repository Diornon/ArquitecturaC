from collections import Counter
from operator import indexOf

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import savefig
from numexpr.necompiler import double

with open('pings', 'r') as file:
    numbers = [line.split("=") for line in file]
nums = []
numbers.pop(0)
for i in numbers:
    print(i[-1].split(" ")[0].strip())

    a = double(i[-1].split(" ")[0].strip())

    nums.append(a)
print(nums.reverse())







plt.plot(nums)
plt.ylabel('Response time in milliseconds')
plt.xlabel('Time in seconds')
plt.title('Grafico')
savefig('Grafico')

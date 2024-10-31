
import matplotlib.pyplot as plt


with open('pings', 'r') as file:
    numbers = [line.split("=") for line in file]
nums = []
numbers.pop(0)
for i in numbers:
    a = double(i[-1].split(" ")[0].strip())

    nums.append(a)

plt.plot(nums)
plt.ylabel('Response time in milliseconds')
plt.xlabel('Time in seconds')
plt.title('Grafico')
savefig('Grafico')

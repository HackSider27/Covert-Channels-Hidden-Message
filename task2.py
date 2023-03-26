import csv
import matplotlib.pyplot as plt
import statistics

times = []
intervals = []

def file_reader(file_name):
    with open(file_name, encoding='utf-8') as r_file:
        dump = csv.reader(r_file, delimiter=",")
        count = 0
        for row in dump:
            if count > 99:
                times.append(row[1])
            count += 1


file_reader('2.csv')

for i in range(len(times)):
    if i != len(times) - 1:
        intervals.append(float(times[i + 1]) - float(times[i]))

distributed_intervals = []
counts = []

temp = 0
while temp < max(intervals) + 1:
    distributed_intervals.append(temp)
    counts.append(0)
    temp += 0.1

print(len(times))
print(len(intervals))
print(len(distributed_intervals))

for i in range(len(intervals)):
    for j in range(len(distributed_intervals)):
        if distributed_intervals[j] < intervals[i] and  intervals[i] < distributed_intervals[j + 1]:
            counts[j] += 1
            break

print(max(counts))

fig, ax = plt.subplots()
ax.bar(distributed_intervals, counts, width=0.09)
plt.show()

# вероятность присутствия скрытого канала стремится к 100% = (1 - 0 / 23) * 100

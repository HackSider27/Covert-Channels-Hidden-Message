import csv
import statistics

def file_reader(file_name):
    with open(file_name, encoding='utf-8') as r_file:
        dump = csv.reader(r_file, delimiter=",")
        count = 0
        for row in dump:
            if count > 99:
                times.append(row[1])
            count += 1


times = []
intervals = []
file_reader('2.csv')

for i in range(len(times)):
    if i != len(times) - 1:
        intervals.append(float(times[i + 1]) - float(times[i]))

print(max(intervals))
print(statistics.mean(intervals))
#print(intervals)

covert_message = ''
for i in range(len(intervals)):
    if intervals[i] < statistics.mean(intervals):
        covert_message += '0'
    else:
        covert_message += '1'

string = ''
for i in range(0, len(covert_message), 8):
    string += chr(int(covert_message[i:i + 8], 2))

print(string)


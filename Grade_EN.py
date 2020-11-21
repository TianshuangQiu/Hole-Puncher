import csv


def compare(a, b):
    string_a = a.strip()
    string_b = b.strip()
    return (string_a.lower() == string_b.lower())


data = []
purged_data = []
regraded = []
correct_answer = ["amiss", "significant", "thesis", "similar", "civilization", "feasible",
                  "persuade", "analyze", "consistent", "police", "hospital", "Pomegranate", "Apple", "Mango"]


with open('data/EN.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        data.append(row)

counter = 0
for row in data:
    if(counter == 0):
        counter += 1
        continue
    buffer = []
    buffer = row[2:49:3]
    purged_data.append(buffer)

for x in purged_data:
    buffer = x[0:2]
    grade = []
    for index, item in enumerate(x[2:]):
        grade.append(compare(item, correct_answer[index]))
    for g in grade:
        if g:
            buffer.append(1)
        else:
            buffer.append(0)
    regraded.append(buffer)

with open("data/Purged_EN.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(regraded)

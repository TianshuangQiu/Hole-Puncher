import csv


def compare(a, b):
    if b == '' or a == '':
        return False
    else:
        string_a = a.strip()
        string_b = b.strip()
        return (string_a == string_b)


data = []
purged_data = []
regraded = []
correct_answer = ["多闻", "芳香", "快乐", "牢靠", "故障", "匪盗",
                  "情投意合", "德育", "有趣", "C.警察", "A.医院", "B.桃子", "B.西瓜", "D.葡萄"]


with open('data/CN.csv', encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        data.append(row)

counter = 0
for row in data:
    if(counter == 0):
        counter += 1
        continue
    buffer = []
    buffer = row[8:-1]
    purged_data.append(buffer)

for x in purged_data:
    buffer = [x[0]]
    grade = []
    for index, item in enumerate(x[1:]):
        grade.append(compare(item, correct_answer[index]))
    for g in grade:
        if g:
            buffer.append(1)
        else:
            buffer.append(0)
    regraded.append(buffer)

with open("data/Purged_CN.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(regraded)

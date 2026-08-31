Data = [[101, "Seema", 45000],
        [340, "Rajani", 13000],
        [210, "Tannu", 14000],
        [320, "Suresh", 35000]]

NewData = []

salary = []

for emp in Data:
    salary.append(emp[2])

salary.sort()

for s in salary:
    for emp in Data:
        if emp[2] == s:
            NewData.append(emp)

print(NewData)

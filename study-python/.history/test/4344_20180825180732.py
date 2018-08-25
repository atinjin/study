tc = int(input())

result = []
for i in range(tc):
    students = input().split()
    total = 0
    points = []
    for j in range(students[1:students.length]):
        point = int(j)
        total += point
        points.append(point)
    count = 0
    for p in points:
        if p > (total/students):
            count = count + 1
    result.append(count/students*100)

for r in result:
    print("{}%".format(r))


tc = int(input())

result = []
for i in range(tc):
    students = [int(x) for x in input().split()]
    print(students)
    total = 0
    points = []
    for point in range(students[1:]):
        total += point
        points.append(point)
    count = 0
    for p in points:
        if p > (total/students):
            count = count + 1
    result.append(count/students*100)

for r in result:
    print("{}%".format(r))


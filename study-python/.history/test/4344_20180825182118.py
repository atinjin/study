tc = int(input())

result = []
for i in range(tc):
    students = [int(x) for x in input().split()]
    print(students)
    total = 0
    points = []
    for point in students[1:]:
        total += point
        points.append(point)
    count = 0
    for p in points:
        if p > (total/len(points)):
            count = count + 1
    result.append(count/len(points)*100)

for r in result:
    print("{.3f}%".format(r))


## N(1 ≤ N ≤ 1000, N은 정수)
## output xx.xxx%
tc = int(input())

result = []
for i in range(tc):
    students = int(input()):
    total = 0
    points = []
    for j in range(students):
        point = int(input())
        total += point
        point.append(point)
    count = 0
    for p in points:
        if p > (total/students):
            count = count + 1
    result.append(count/students*100)

for r in result:
    print("{}%".format(r))


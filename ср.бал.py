grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
#print(sorted(students))
a= {}
for i in range(len(grades)):a[sorted_students[i]] = grades[i]
#print(a)
#res = {grades: sorted_students for i in range(len(grades))}
#print("The original dictionary is : " + str(a))
res = dict()
for key in a:
    res[key] = sum(a[key]) / len(a[key])
print(str(res))

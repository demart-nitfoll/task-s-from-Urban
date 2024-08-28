grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
sred_bal = {}
for i in range(len(students)):
    sred_bal[students[i]] = sum(grades[i]) / len(grades[i])
print(sred_bal)
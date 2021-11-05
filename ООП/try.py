def re():
    summa_grades = 0
    count_grades = 0
    for i in self.grades.values():
        while i in range(0, 11):
            summa_grades += i
            count_grades += 1
    return (summa_grades / count_grades)


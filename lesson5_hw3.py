try:
    with open('salary_per_employee.txt', 'r', encoding='utf8') as sal:
        num_lines = 0
        sal_sum = 0
        for line in sal:
            line = line.strip("\n")
            num_lines += 1
            emp_sal = line.split()
            x = int(emp_sal[1])
            if x < 20000:
                print(emp_sal[0])
            sal_sum += x
except IOError as err:
    print(f'IOError: {err}')

print(f"Средняя величина дохода: {sal_sum / num_lines}")

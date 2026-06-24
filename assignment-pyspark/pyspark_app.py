from pyspark import SparkContext

sc = SparkContext("local", "EmployeeRDD")

# Read CSV
data = sc.textFile("employee_data.csv")

header = data.first()

employees = data.filter(lambda x: x != header) \
    .map(lambda x: x.split(",")) \
    .map(lambda x: {
        "id": int(x[0]),
        "name": x[1],
        "department": x[2],
        "salary": int(x[3])
    })

# 1. Sort by salary descending
print("\n===== Employees Sorted by Salary =====")

sorted_emp = employees.sortBy(
    lambda x: x["salary"],
    ascending=False
)

for emp in sorted_emp.collect():
    print(emp)

# 2. Department wise salary total
print("\n===== Department Wise Salary Total =====")

dept_salary = employees.map(
    lambda x: (x["department"], x["salary"])
).reduceByKey(
    lambda a, b: a + b
)

for dept in dept_salary.collect():
    print(dept)

# 3. Top 3 highest paid employees
top3 = sorted_emp.take(3)

with open("output/top3_employees.txt", "w") as f:
    for emp in top3:
        f.write(str(emp) + "\n")

print("\nTop 3 employees saved to output/top3_employees.txt")

sc.stop()
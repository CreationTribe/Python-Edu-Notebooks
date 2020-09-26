# storing shit in lists

temps = [55, 66, 55, 75, 23, 34, 54, 98]

for tmp in temps:
    print("Welcome to % s" % tmp)
    # print("Temp for whatever day: % "% tmp)

# computing number of days in a year

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

num_days = 0
for i in range(12):
    days_in_month = days_in_months[i]
    num_days += days_in_month
    # you need to use the string '% s' for the string replacement to work
    print("Days in month #% s: % s | Total so far: % s" % (i, days_in_month, num_days))
print("Days in year: {}".format(num_days))

num_days = 0
for i in range(len(days_in_months)):
    num_days += days_in_months[i]
    print("Days in month #{n1}: {n2} | Total so far: {n3}".format(n1=i, n2=days_in_month, n3=num_days))
print(f"Days in year: {num_days}")

# in-line arithmetic
print(f"(2*3)-10 = {(2*3)-10}")

# interpolation with the string template module
from string import Template
dayTemplate = Template('$n1 in a year')

num_days = 0
for i in days_in_months:
    num_days += i

print(dayTemplate.substitute(n1=num_days))

# summing a list without looping
num_days = sum(days_in_months)
print(num_days)


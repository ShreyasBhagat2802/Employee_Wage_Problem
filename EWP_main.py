print("Welcome to Employee Wage Computation Program on Master Branch")

#UC1
import random 
attendance = random.randint(0, 1)
    
if attendance == 1:
    print("Employee is Present")
else:
    print("Employee is Absent")

#UC2
wage_per_hour = 20
full_day_hours = 8
    
full_time_wage = wage_per_hour * full_day_hours
    
print(full_time_wage)

#UC3
part_time_hours = 8
    
part_time_wage = wage_per_hour * part_time_hours
    
print(part_time_hours)

#UC4
def employee_type():
    employee_status = random.randint(0, 2)
    
    match employee_status:
        case 2:
            return "full-time"
        case 1:
            return "part-time"
        case _:
            return "absent"

employee_state = employee_type()
if employee_state == "full-time":
    print("Employee is Full Time. Wage: ", {full_time_wage})
elif employee_state == "part-time":
    print("Employee is Part Time. Wage: ", {part_time_wage})
else:
    print("Employee is Absent.")

#UC5
working_days_per_month = 20
month_wage = 0
if employee_state == "full-time":
    month_wage = working_days_per_month * full_time_wage
elif employee_state == "part-time":
    month_wage = working_days_per_month * part_time_wage
print("Month wage is : ", month_wage)

#UC6
max_working_hours = 100
max_working_days = 20

total_working_hours = 0
total_working_days = 0
total_wages = 0

while total_working_hours < max_working_hours and total_working_days < max_working_days:
    
    work_hours = random.choice([0, 4, 8])
    
    total_working_hours += work_hours
    total_working_days += 1

    total_wages += work_hours * wage_per_hour

print(f"Day {total_working_days}: Worked {work_hours} hours, Total hours: {total_working_hours}, Wages: {total_wages}")

#UC7
class EmployeeWageComputation:
    wage_per_hour = 20
    full_day_hour = 8
    part_time_hour = 4

    @classmethod
    def calculate_wage(cls, employee_type):
        if employee_type == 1:
            return cls.full_day_hour * cls.wage_per_hour
        elif employee_type == 2:
            return cls.part_time_hour * cls.wage_per_hour
        else:
            return 0

employee_type = random.choice([0, 1, 2])
employee_daily_wage = EmployeeWageComputation.calculate_wage(employee_type)

print(f"Employee Wage: {employee_daily_wage}")